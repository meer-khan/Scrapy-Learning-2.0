# import scrapy
# from jessops.items import JessopsItem

# class DronesSpider(scrapy.Spider):
#     name = 'drones'
#     allowed_domains = ['jessops.com']
#     start_urls = ['http://jessops.com/drones']

#     def parse(self, response):
#         products = response.css('div.details-pricing')
#         # print("Products we have: ", products)
#         for product in products:
#             # print("Products we have: ", product)
#             item = {
#                 "name" : product.css('a::text').get(),
#                 'price' : product.css('p.price.larger::text').get().replace(",", "")
#             }
#             yield item



# import scrapy
# from jessops.items import JessopsItems
# from scrapy.loader import ItemLoader

# class DronesSpider(scrapy.Spider):
#     name = 'drones'
#     allowed_domains = ['jessops.com']
#     start_urls = ['http://jessops.com/drones']
    
#     def parse(self, response):
#         item = JessopsItems()
#         products = response.css('div.products-list.list-view')
#         # item['name'] =  products.css("h4").css("a::text").getall()
#         # item['price'] = products.css('p.price.larger::text').getall()
#         for product in products:
#             item['name'] =  product.css("h4").css("a::text").getall()
#             item['price'] = product.css('p.price.larger::text').getall()
#             yield item


import scrapy
from jessops.items import JessopsItems
from scrapy.loader import ItemLoader

class DronesSpider(scrapy.Spider):
    name = 'drones'
    allowed_domains = ['jessops.com']
    start_urls = ['http://jessops.com/drones']
    
    def parse(self, response):
        products = response.css('div.products-list.list-view')
        for product in products:
            l = ItemLoader(item= JessopsItems(), selector = product)
            l.add_css('name', 'a')
            l.add_css('price', 'p.price.larger')
            # item['name'] =  product.css("h4").css("a::text").getall()
            # item['price'] = product.css('p.price.larger::text').getall()
            yield l.load_item()


SLE+X771t/eRycudllvYQHEPS6WhCuFSHs4WGUFCCoKManBTBHKcb9o/D2PKBocS9myUsaZS8S3UTc+MS9t06A==

SLE+X771t/eRycudllvYQHEPS6WhCuFSHs4WGUFCCoKManBTBHKcb9o/D2PKBocS9myUsaZS8S3UTc+MS9t06A==

"L5SlkAOI7nnfXY8+63GpvExHHuq3qSeeCdxpJV1UOUZPoYBDwhGWsVoyG3oxdv2YrAv5WZQ4w8vRx+v8eTq6yA=="