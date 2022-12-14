import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    # allowed_domains = ['amazon.com']

    start_urls = ['https://www.amazon.in/Books-DEPARTMENT/s?rh=n%3A976389031%2Cp_27%3ADEPARTMENT']

    def parse(self, response):
        items = AmazontutorialItem()
        
        items["productName"] = response.css(".a-size-medium.a-color-base.a-text-normal::text").get()
        items["productAuthor"] = response.css(".a-size-base.a-color-secondary::text").get()
        items["productPrice"] = response.css(".a-price-whole::text").get()
        items["productImageLink"] = response.css(".s-image::attr(src)").get()

        yield items