import scrapy

from ..items import MatlabItem

# class WhiskeySpider(scrapy.Spider):
#     name = 'matlab'
#     start_urls = [
#         'https://www.mathworks.com/matlabcentral/fileexchange/?sort=date_desc_updated']

#     def parse(self, response):
#         for items in response.css('div.card_container'):
#             yield {
#                 "RepoName": items.css('h3::text').get(),
#                 "Downloads": items.css('div.metadata_info.pull-left').css("p::text").get(),
#                 "RepoLink": items.css("div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width").css("a").attrib["href"]

#             }

#         nextPage = response.css(
#             "div.col-xs-12").css("a.btn.btn_color_blue").attrib["href"]
#         if nextPage is not None:
#             yield response.follow(nextPage, callback=self.parse)



class WhiskeySpider(scrapy.Spider):

    name = 'matlab'
    state = ""
    countglobal = 0
    start_urls = [
        'https://www.mathworks.com/matlabcentral/fileexchange/?sort=date_desc_updated']

    # def parse(self, response):
    #     # print ("URL: " + response.request.url)
    #     # if response.request.url == 'https://www.mathworks.com/matlabcentral/fileexchange/?page=7&sort=date_desc_updated':
    #     for items in response.css('div.card_container'):
    #         RepoLink = items.css("div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width").css("a").attrib["href"]
    #         results = {
    #             "RepoName": items.css('h3::text').get(),
    #             "Downloads": items.css('div.metadata_info.pull-left').css("p::text").get(),
    #             "RepoLink": items.css("div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width").css("a").attrib["href"]

    #         }
    #     #     RepoInside = response.follow(nextPage, callback=self.parse)
    #     # else: 
    #     #     if RepoLink is not None: 
                


    #         yield results

    #     nextPage = response.css(
    #         "div.col-xs-12").css("a.btn.btn_color_blue").attrib["href"]
    #     if nextPage is not None:
    #         yield response.follow(nextPage, callback=self.parse)


    def parse(self, response):
        count = 0
        for items in response.css('div.card_container'):
            RepoLink = items.css("div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width").css("a").attrib["href"]
            # results = {
            #     "RepoName": items.css('h3::text').get(),
            #     "Downloads": items.css('div.metadata_info.pull-left').css("p::text").get(),
            #     "RepoLink": items.css("div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width").css("a").attrib["href"]
            # }
            # if RepoLink is not None: 
            #     results = scrapy.Request(url = "https://www.mathworks.com"+RepoLink,callback=self.repoDetails("https://www.mathworks.com"+RepoLink))
            #     print("RESULTS", results)
            #     results["functions"] = results
            ok = response.follow(RepoLink,callback=self.parse_repositories)
            count += 1
            print(f"DAAAATAAAAAAA  {count}", type(ok))
            yield response.follow(RepoLink,callback=self.parse_repositories)

        nextPage = response.css(
            "div.col-xs-12").css("a.btn.btn_color_blue").attrib["href"]
        if nextPage is not None:
            yield response.follow(nextPage, callback=self.parse)

    
    def parse_repositories(self,response): 
        items = MatlabItem()
        self.countglobal += 1
        print(f"TYPEEEE {self.countglobal}" , type(response))

        repoName = response.css("span#titleText::text").get()
        repoVersion = response.css("div.add_margin_5 span.small.add_font_color_mediumgray::text").get()
        authorName = response.css("a.author_inline.analyticsMlcProfileModal.results_author::text").get()
        downloads = response.css("span#downloads::text").get()
        githubLicense = response.css("p.add_margin_5.github_license.text-right").css("a::attr(href)").get()
        functionLinks = response.css("div.package__file-list.single_tier.functions").css("a::attr(href)").getall()
        functionName = response.css("div.package__file-list.single_tier.functions").css("a::text").getall()
        items["repoName"] = repoName
        items["repoVersion"] = repoVersion
        items["authorName"] = authorName
        items["downloads"] = downloads
        items["githubLink"] = githubLicense
        items["functionLinks"] = functionLinks
        items["functionName"] = functionName

        
        # yield        {
        #     "repoName" : response.css("span#titleText::text").get(),
        #     "repoVersion" : response.css("div.add_margin_5 span.small.add_font_color_mediumgray::text").get(),
        #     "authorName" : response.css("a.author_inline.analyticsMlcProfileModal.results_author::text").get(),
        #     "downloads" : response.css("span#downloads::text").get(),
        #     "functionLinks" : response.css("div.package__file-list.single_tier.functions").css("a::attr(href)").getall(),
        #     "functionName" : response.css("div.package__file-list.single_tier.functions").css("a::text").getall()
        # }
        yield items


# response.css("ul.nav.nav-list.nav--file-list.truncate_text.list-inline").css("li").css("a::text").getall()

