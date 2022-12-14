# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazontutorialItem(scrapy.Item):
    # define the fields for your item here like:
    productName = scrapy.Field()
    productAuthor = scrapy.Field()
    productPrice = scrapy.Field()
    productImageLink = scrapy.Field()


    
