# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TimocomItem(scrapy.Item):
    freights = scrapy.Field()
    origin = scrapy.Field()
    destination = scrapy.Field()
    last_updated = scrapy.Field()