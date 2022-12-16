
import scrapy
from scrapy_splash import SplashRequest 
import base64

# lua_script = """
# function main(splash, args)
#     splash:init_cookies(splash.args.cookies)
#     assert(splash:go(args.url))
#     assert(splash:wait(3))
#     splash:set_viewport_full()
#     local email_input = splash:select('input[name=email]')   
#     email_input:send_text("shahmirkhan519@gmail.com")
#     assert(splash:wait(3))
#     local email_submit = splash:select('input[id=continue]')
#     email_submit:click()
#     assert(splash:wait(5))
#     local password_input = splash:select('input[name=password]')   
#     password_input:send_text("iiui1111S")
#     assert(splash:wait(3))
#     local password_submit = splash:select('input[id=signInSubmit]')
#     password_submit:click()
#     assert(splash:wait(5))
#     return {
#         html=splash:html(),
#         url = splash:url(),
#         png = splash:png(),
#         cookies = splash:get_cookies(),
#         }
#     end
# """


# lua_script = """
# function main(splash, args)
#     splash:init_cookies(splash.args.cookies)
#     assert(splash:go(args.url))
#     assert(splash:wait(1))
#     splash:set_viewport_full()
#     local email_input = splash:select('input[name=email]')   
#     email_input:send_text("shahmirkhan519@gmail.com")
#     assert(splash:wait(1))
#     local email_submit = splash:select('input[id=continue]')
#     email_submit:click()
#     assert(splash:wait(3))
#     local password_input = splash:select('input[name=password]')   
#     password_input:send_text("iiui1111S")
#     assert(splash:wait(1))
#     local password_submit = splash:select('input[id=signInSubmit]')
#     password_submit:click()
#     assert(splash:wait(3))
#     return {
#         html=splash:html(),
#         url = splash:url(),
#         png = splash:png(),
#         cookies = splash:get_cookies(),
#         }
#     end
# """




# class HeadlessBrowserLoginSpider(scrapy.Spider):
#     name = "matlab_login"

#     def start_requests(self):
#         signin_url = 'https://www.mathworks.com/login?uri=https%3A%2F%2Fwww.mathworks.com%2Fmatlabcentral%2Ffileexchange%2F121852-fatty-liver-level-recognition-using-pso'
#         yield SplashRequest(
#             url=signin_url, 
#             callback=self.start_scrapping,
#             endpoint='execute', 
#             args={
#                 'width': 1000,
#                 'lua_source': lua_script,
#                 'ua': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
#                 },
#             )
    
#     def start_scrapping(self,response):
#         imgdata = base64.b64decode(response.data['png'])
#         filename = 'after_login.png'
#         with open(filename, 'wb') as f:
#             f.write(imgdata)

#         cookies_dict = {cookie['name']: cookie['value'] for cookie in response.data['cookies']}
#         url_list = ['https://www.mathworks.com/matlabcentral/fileexchange/']
#         for url in url_list:
#             yield scrapy.Request(url=url, cookies=cookies_dict, callback=self.parse)

#     def parse(self, response):
#         # save the full page html
#         with open('response.html', 'wb') as f:
#             f.write(response.body)

#         # scraping all the links on the page
#         page_urls = response.css('a')
#         for page_url in page_urls:
#             if(page_url.css('a::text').get() is not None):
#                 try:
#                     yield {
#                         'url_text' : page_url.css('a::text').get(),
#                         'url' : page_url.css('a').attrib['href']
#                     }
#                 except:
#                     print("An error occurred when scraping a link")







import scrapy 
from scrapy_splash import SplashRequest
import base64




lua_script = """
function main(splash, args)
    print ("OKEYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    splash:init_cookies(splash.args.cookies)
    assert(splash:go(args.url))
    assert(splash:wait(1))
    splash:set_viewport_full()
    local email_input = splash:select('input[name=userId]')   
    email_input:send_text("shahmirkhan519@gmail.com")
    assert(splash:wait(1))
    local email_submit = splash:select('input[id=submit_identifier]')
    email_submit:click()
    assert(splash:wait(3))
    local password_input = splash:select('input[name=password]')   
    password_input:send_text("iiui1111S")
    assert(splash:wait(1))
    local password_submit = splash:select('button[name=submit]')
    password_submit:click()
    assert(splash:wait(3))
    return {
        html=splash:html(),
        url = splash:url(),
        png = splash:png(),
        cookies = splash:get_cookies(),
        }
    end
"""

class HeadlessBrowserLoginSpider(scrapy.Spider):
    name = "matlab_login2"

    def start_requests(self):
        signin_url = 'https://www.mathworks.com/login?uri=https%3A%2F%2Fwww.mathworks.com%2Fhelp%2Fthingspeak%2Frest-api.html'
        print("IIIIIIIIIIIIIIIII AAAAAMMMMMMMMMMMMMMMMMMMMMM HEREEEEEEEEEEEEEEEEEEEEEEEEE")        
        yield SplashRequest(
            url=signin_url, 
            callback=self.start_scrapping,
            # endpoint='execute', 
            args={
                'wait': 0.5,
                'width': 1000,
                'lua_source': lua_script,
                'url': 'https://www.mathworks.com/login?uri=https%3A%2F%2Fwww.mathworks.com%2Fhelp%2Fthingspeak%2Frest-api.html'
                # 'ua': "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                },
            )
    
    def start_scrapping(self,response):
        imgdata = base64.b64decode(response.data['png'])
        filename = 'after_login.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)

        cookies_dict = {cookie['name']: cookie['value'] for cookie in response.data['cookies']}
        url_list = ['https://www.mathworks.com/matlabcentral/fileexchange/?sort=date_desc_updated']
        for url in url_list:
            yield scrapy.Request(url=url, cookies=cookies_dict, callback=self.parse)


    def parse(self, response):
        # save the full page html
        with open('response.html', 'wb') as f:
            f.write(response.body)

        # scraping all the links on the page
        page_urls = response.css('a')
        for page_url in page_urls:
            if(page_url.css('a::text').get() is not None):
                try:
                    yield {
                        'url_text' : page_url.css('a::text').get(),
                        'url' : page_url.css('a').attrib['href']
                    }
                except:
                    print("An error occurred when scraping a link")
