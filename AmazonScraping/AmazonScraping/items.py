# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    prices = scrapy.Field()
    priceFromates = scrapy.Field()
    rating = scrapy.Field()

    pass
