# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MatlabItem(scrapy.Item):
    # define the fields for your item here like:
    repoName = scrapy.Field()
    repoVersion = scrapy.Field()
    authorName = scrapy.Field()
    downloads = scrapy.Field()
    githubLink = scrapy.Field()
    functionLinks = scrapy.Field()
    functionName = scrapy.Field()



