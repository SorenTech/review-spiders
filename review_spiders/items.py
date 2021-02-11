# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ReviewSpidersItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    authors = Field()
    date = Field()
    topic = Field()
    tags = Field()
    content = Field()
    copyright = Field()

