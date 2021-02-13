# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ReviewItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    publisher = Field()
    weight = Field()
    date = Field()
    url = Field()
    title = Field()
    authors = Field()
    topic = Field()
    tags = Field()
    content = Field()
    copyright = Field()

