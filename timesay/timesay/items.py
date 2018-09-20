# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TimesayItem(scrapy.Item):
    # define the fields for your item here like:
    money = scrapy.Field()
    pass

class TimesayUrlItem(scrapy.Item):
    url=scrapy.Field()
    pass

class TimesayWinItem(scrapy.Item):
    winPercentage=scrapy.Field()
    money=scrapy.Field()
    pass