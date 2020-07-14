# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TabledatascrapingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    runs = scrapy.Field()
    country =scrapy.Field()
    span = scrapy.Field()
    matchesPlayes = scrapy.Field()
    inningsBatted = scrapy.Field()
    notOuts = scrapy.Field()
    highestInningScore = scrapy.Field()
    average = scrapy.Field()
    pass
