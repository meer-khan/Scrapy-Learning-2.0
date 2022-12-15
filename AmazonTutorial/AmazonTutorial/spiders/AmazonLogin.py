# import scrapy
# from ..items import AmazontutorialItem
# from scrapy_splash import SplashRequest
# import base64

# class HeadlessBrowserLoginSpider(scrapy.Spider):
#     name = "amazon_login"












import scrapy
from scrapy_splash import SplashRequest 
import base64

lua_script = """
function main(splash, args)
    splash:init_cookies(splash.args.cookies)
    assert(splash:go(args.url))
    assert(splash:wait(3))
    splash:set_viewport_full()
    local email_input = splash:select('input[name=email]')   
    email_input:send_text("shahmirkhan519@gmail.com")
    assert(splash:wait(3))
    local email_submit = splash:select('input[id=continue]')
    email_submit:click()
    assert(splash:wait(5))
    local password_input = splash:select('input[name=password]')   
    password_input:send_text("Pakistan2212")
    assert(splash:wait(3))
    local password_submit = splash:select('input[id=signInSubmit]')
    password_submit:click()
    assert(splash:wait(5))
    return {
        html=splash:html(),
        url = splash:url(),
        png = splash:png(),
        cookies = splash:get_cookies(),
        }
    end
"""


class HeadlessBrowserLoginSpider(scrapy.Spider):
    name = "amazon_login"

    def start_requests(self):
        signin_url = 'https://www.amazon.ae/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.ae%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_top_flyout_signout&openid.assoc_handle=aeflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
        yield SplashRequest(
            url=signin_url, 
            callback=self.start_scrapping,
            endpoint='execute', 
            args={
                'width': 1000,
                'lua_source': lua_script,
                'ua': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
                },
            )
    
    def start_scrapping(self,response):
        imgdata = base64.b64decode(response.data['png'])
        filename = 'after_login.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)

        cookies_dict = {cookie['name']: cookie['value'] for cookie in response.data['cookies']}
        url_list = ['https://www.amazon.com/']
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