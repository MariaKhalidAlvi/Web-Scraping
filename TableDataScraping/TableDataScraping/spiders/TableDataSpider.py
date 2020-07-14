#libraries
import scrapy
from ..items import TabledatascrapingItem

# Spider to scrape table data from stats.espncricinfo.com of Crickters for test matches
#Data includes Name. conuntry, span, runs, innings, average,notOuts ,matchesPlayes and inningsBatted
# Also implements pagination to scrape data from all pages

class TableDataSpider(scrapy.Spider):

    name = "TableData"   #name of spider to crawl
    start_urls = ["https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;template=results;type=batting"]   # start url
    pageNo = 1   # for pagination


    custom_settings = {
        'FEED_FORMAT': 'csv',  # data type of output file
        'FEED_URI': 'CricketTest_TableData.csv'   # Name and location of output file
    }



    def parse(self, response):   # funtion to scrape data
        self.items = TabledatascrapingItem()  # scrapy objects that define key-value pairs


        rows = response.css("table.engineTable tr.data1")  # extracts each row containing all data fields

        for row in rows:  # loop over all rows

            self.items['name'] = row.css("a.data-link::text").extract()
            self.items['runs'] = row.css("td b::text").extract()
            remainingData = row.css("td::text").extract()
            self.items['country'] = remainingData[0]
            self.items['span'] =remainingData[1]
            self.items['matchesPlayes'] = remainingData[2]
            self.items['inningsBatted'] = remainingData[3]
            self.items['notOuts'] = remainingData[4]
            self.items['highestInningScore'] = remainingData[5]
            self.items['average'] = remainingData[6]

            yield self.items   #yield data to csv file

        #Pagination code
        self.pageNo = self.pageNo + 1
        nextPage = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;page="+str(self.pageNo)+";template=results;type=batting"
        if self.pageNo <= 61:  # loop till last page
            yield response.follow(nextPage,callback=self.parse)  # call back for next page if exists







