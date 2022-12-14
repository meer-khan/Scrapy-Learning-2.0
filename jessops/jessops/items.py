import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def removeSpaces(value):
    return value.strip()
class JessopsItems(scrapy.Item):
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst() )
    price = scrapy.Field(input_processor = MapCompose(remove_tags, removeSpaces), output_processor = TakeFirst())