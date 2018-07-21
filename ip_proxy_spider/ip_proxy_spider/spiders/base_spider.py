# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ip_proxy_spider.const import *
from ip_proxy_spider.spiders.parse_methods import ParseMethodBase


class BaseSpider(scrapy.Spider):
    name = 'base_spider'

    allowed_domains = []

    start_urls = []

    def start_requests(self):
        # 从配置的网址开始遍历
        for url, name, inland in SOURCE_URL:
            yield Request(url, callback=self.parse, meta={'name': name, 'inland': inland})                

    def parse(self, response):
        name = response.meta['name']

        for cls in ParseMethodBase.__subclasses__():
            cls_name = cls.__name__
            if cls_name == name:
                gen = cls.parse(cls, response)
                for x in gen:
                    yield x
            else:
                print('未找到【%s】对应的解析函数' % name)