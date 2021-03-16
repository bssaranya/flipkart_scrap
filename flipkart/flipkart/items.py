# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    item_company = scrapy.Field()
    item_price = scrapy.Field()
    item_size = scrapy.Field()
