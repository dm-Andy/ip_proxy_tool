# ==========================================================================================
# ParseMethodBase：
# 所有解析函数的基类，必须继承此类，否则无法解析

# 子类的class name必须与const.py里面SOURCE_URL配置的name一致
# ==========================================================================================
from scrapy import Request
from ip_proxy_spider.items import IpProxyItem
import re


class ParseMethodBase:
    pass

class kuaidaili(ParseMethodBase):
    def parse(self, response):
        print(response.url)
        trs = response.xpath('//*[@id="freelist"]//tbody/tr')

        for tr in trs:
            item = IpProxyItem()

            item['ip'] = tr.xpath('./td[@data-title="IP"]/text()').extract_first()
            item['port'] = tr.xpath('./td[@data-title="PORT"]/text()').extract_first()
            item['anonymity'] = tr.xpath('./td[@data-title="匿名度"]/text()').extract_first()
            type_ = tr.xpath('./td[@data-title="类型"]/text()').extract_first()
            item['location'] = tr.xpath('./td[@data-title="位置"]/text()').extract_first()

            item['https'] = 'yes' if type_.lower().find('https') != -1 else 'no'

            yield item
            
        name = response.meta['name']
        inland = response.meta['inland']

        count = int(re.search(r'proxylist/(\d+)', response.url).group(1))
        if count < 10:
            url = re.sub(r'proxylist/(\d+)', 'proxylist/' + str(count + 1), response.url, 1)
            yield Request(url, meta={'name': name, 'inland': inland})