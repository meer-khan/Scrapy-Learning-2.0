import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    # allowed_domains = ['amazon.com']

    start_urls = ['https://www.amazon.in/Books-DEPARTMENT/s?rh=n%3A976389031%2Cp_27%3ADEPARTMENT']

    def parse(self, response):
        items = AmazontutorialItem()
        
