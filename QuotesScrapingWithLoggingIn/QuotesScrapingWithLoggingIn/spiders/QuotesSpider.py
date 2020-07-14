#libraries
import scrapy
from scrapy.http import FormRequest
from ..items import QuotesscrapingItem

# Spider to scrape data from http://quotes.toscrape.com/
#Data includes quote, author, and tags
# Also implements pagination to scrape data from all pages

class QuotesSpider(scrapy.Spider):

    name = "QuotesWithLogin"  # name of spider to crawl
    start_urls = ['http://quotes.toscrape.com/login']  # start url

    custom_settings = {
        'FEED_FORMAT': 'csv',  # data type of output file
        'FEED_URI': 'QuotesData.csv'   # Name and location of output file
    }


    def parse(self, response):


        csrf_token = response.css("form input::attr(value)").extract()[0]   # retrive csrf token for auto login

        return FormRequest.from_response(response, formdata={    # request for login and call funtion to work on received response
            'csrf_token':csrf_token,
            'username': "Maria",
            'password':"Password"
        }, callback = self.scrapeData)

    def scrapeData(self, response):   # function to scrape data from response

        self.items = QuotesscrapingItem()  # scrapy objects that define key-value pairs

        quoteInfoDivs = response.css("div.quote")      # retrive quote divs


        for quoteDiv in quoteInfoDivs:      # loop over all the retrived divs of quotes

            self.items["quote"] = quoteDiv.css("span.text::text").extract()    # extract quote
            self.items["author"] = quoteDiv.css("small.author::text").extract()    # extract author
            # authorLink = response.css("span a::attr(href)").extract()
            self.items["tags"] = quoteDiv.css("a.tag::text").extract()     # extract tags

            yield self.items

            # Pagination code
            nextPage = response.css('li.next a::attr(href)').get()  # get link for next page
            if nextPage is not None:
                print("NextPage Exists")
                yield response.follow(nextPage, callback=self.scrapeData)  # call back for next page if exists


