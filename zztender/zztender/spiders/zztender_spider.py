import scrapy
from scrapy import Selector

from zztender.items import ZztenderItem


def handle_addr(addres):
    addres = [x.strip() for x in addres]
    return addres

def split_selector(n_c):
    n_c = [x.split("/") for x in n_c]
    return n_c

class ZztenderSpiderSpider(scrapy.Spider):
    name = 'zztender_spider'
    allowed_domains = ['www.zztender.com/tender/5bf4e003ebfca']
    start_urls = ['http://www.zztender.com/tender/5bf4e003ebfca']

    page_No = 1
    url = 'http://www.zztender.com/tender/5bf4e003ebfca/?&page=%d'

    def parse(self, response):
        selector = Selector(response)
        # 获取页数
        page_Count = selector.xpath("/html/body/div[@class='module4']/div[@class='container']/div[@class='row']/div[@class='col-md-9']/ul[1]/li/span/text()").extract()
        page_Count = int(split_selector(page_Count)[0][1])
        # print(page_Count)

        li_list = selector.xpath("/html/body/div[@class='module4']/div[@class='container']/div[@class='row']/div[@class='col-md-9']/div[2]/ul/a").extract()
        r = 1
        for li in li_list:
            item = ZztenderItem()
            item['title'] = selector.xpath("/html/body/div[@class='module4']/div[@class='container']/div[@class='row']/div[@class='col-md-9']/div[2]/ul/a[{}]/@title".format(r)).extract()
            item['start_time'] = selector.xpath("/html/body/div[@class='module4']/div[@class='container']/div[@class='row']/div[@class='col-md-9']/div[2]/ul/a[{}]/li/span[2]/text()".format(r)).extract()
            item['end_time'] = selector.xpath("/html/body/div[@class='module4']/div[@class='container']/div[@class='row']/div[@class='col-md-9']/div[2]/ul/a[{}]/li/span[1]/text()".format(r)).extract()
            item['url'] = selector.xpath("/html/body/div[@class='module4']/div[@class='container']/div[@class='row']/div[@class='col-md-9']/div[2]/ul/a[{}]/@href".format(r)).extract()
            # print(item)
            yield item
            r += 1

        if self.page_No < page_Count:
            self.page_No+=1
            url = format(self.url % self.page_No)
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            yield request