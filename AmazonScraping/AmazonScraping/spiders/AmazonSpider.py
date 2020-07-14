#libraries
import scrapy
from ..items import AmazonscrapingItem

# Spider to scrape data from Amazon for all the book posts from last 30 days
#Data includes Title, rating, price type and price of books
# Also implements pagination to scrape data from all pages

class AmazonSpider(scrapy.Spider):

    name = "Amazon"   #name of spider to crawl
    start_urls = ['https://www.amazon.com/s?k=books+last+30+days&ref=nb_sb_noss']   # start url



    custom_settings = {
        'FEED_FORMAT': 'csv',  # data type of output file
        'FEED_URI': 'AmazonBooksData.csv'   # Name and location of output file
    }



    def parse(self, response):   # funtion to scrape data
        self.items = AmazonscrapingItem()  # scrapy objects that define key-value pairs

        for box in response.xpath("//div[@class='sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28']"):  #loop over div sections containing details of each book

            self.items["title"] = box.css(".a-color-base.a-text-normal::text").extract()  # extract title
            self.items["priceFromates"] = box.css(".a-link-normal.a-text-bold::text").extract()  # extract all the Price types such as Hardcover, kindle etc
            self.items["prices"] = box.css(".a-price span span::text").extract()   # extract all the Prices
            self.items["rating"] = box.css(".a-icon-alt::text").extract()   # extract Ratinnf

            yield self.items                       # yield all teh data into output file

        #Pagination code
        nextPage = response.css('li.a-last a::attr(href)').get()  # get link for next page
        if nextPage is not None:
            print("NextPage Exists")
            yield response.follow(nextPage,callback=self.parse)  # call back for next page if exists







