#libraries
import scrapy
from scrapy_splash import SplashRequest
from ..items import JavascriptpagesscrapingItem

# Spider to scrape data from http://quotes.toscrape.com/ but specifically for Java Script Pages
#It uses docker image of scrapy-splash to render the pages of JavaScript and get the response back for scraping
#Data includes quote, author, and tags
# Also implements pagination to scrape data from all pages

class QuotesSpider(scrapy.Spider):

    name = "QuotesJSPages"  # name of spider to crawl  # start url
    custom_settings = {
        'FEED_FORMAT': 'csv',  # data type of output file
        'FEED_URI': 'QuotesDataJSPages.csv'   # Name and location of output file
    }

    def __init__(self):
        self.url = []
        for i in range(1,11):
            self.url.append("http://quotes.toscrape.com/js/page/"+str(i)+"/")   #intialize a list of urls for pagination

    def start_requests(self):

        for url in self.url:      # loop over all the urls for pagination

            yield SplashRequest(        # sends request to splash docker image to render the pages of JavaScript
                                        # and send response to parse for scraping
                url= url,
                callback= self.parse,
             )

    def parse(self, response):

        self.items = JavascriptpagesscrapingItem()  # scrapy objects that define key-value pairs

        quoteInfoDivs = response.css("div.quote")      # retrive quote divs


        for quoteDiv in quoteInfoDivs:      # loop over all the retrived divs of quotes

            self.items["quote"] = quoteDiv.css("span.text::text").extract()    # extract quote
            self.items["author"] = quoteDiv.css("small.author::text").extract()    # extract author
            # authorLink = response.css("span a::attr(href)").extract()
            self.items["tags"] = quoteDiv.css("a.tag::text").extract()     # extract tags

            yield self.items



