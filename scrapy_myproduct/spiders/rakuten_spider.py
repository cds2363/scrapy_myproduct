# -*- coding: utf-8 -*-
import scrapy


class RakutenSpiderSpider(scrapy.Spider):
    name = 'SearchRakutenProduct'
    allowed_domains = ['search.rakuten.co.jp']
    start_urls = ['https://search.rakuten.co.jp/search/mall/uc-0358/']

    def parse(self, response):
        for item in response.xpath('//div[@class="dui-card searchresultitem"]'):
            item.xpath('//div[@class="content title"]/h2/a').get()
            
        pass
