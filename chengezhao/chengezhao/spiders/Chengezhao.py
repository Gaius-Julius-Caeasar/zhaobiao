import json

import scrapy
from scrapy import Selector

from chengezhao.items import ChengezhaoItem

def url_Splicing(url_1,url_2):
    url_Splicing = [url_1+x for x in url_2]
    return url_Splicing


class ChengezhaoSpider(scrapy.Spider):
    name = 'Chengezhao'
    allowed_domains = ['chengezhao.com/cms/channel/ywgg/index.htm']
    start_urls = ['http://www.chengezhao.com/cms/channel/ywgg/index.htm?pageNo=1']

    pageNum = 1
    url = 'http://www.chengezhao.com/cms/channel/ywgg/index.htm?pageNo=%d'


    def parse(self, response):
        selector = Selector(response)

        # 获取页数
        page_Count = int(selector.xpath('/html/body/div[@class="cez-business-main"]/div[@class="cez-business-main-wrapper cez-main-content"]/div[@class="cez-business-main__content"]/div[@class="cez-business-main__news"]/div[@class="cez-comp-pagination"]/@data-page-total').extract()[0])
        # print(page_Count)

        li_list = selector.xpath('/html/body/div[@class="cez-business-main"]/div[@class="cez-business-main-wrapper cez-main-content"]/div[@class="cez-business-main__content"]/div[@class="cez-business-main__news"]/div').extract()
        r = 0
        for li in li_list:
            r += 1
        for i in range(r-1):
            item = ChengezhaoItem()
            i += 1
            item['create_time'] = selector.xpath('/html/body/div[@class="cez-business-main"]/div[@class="cez-business-main-wrapper cez-main-content"]/div[@class="cez-business-main__content"]/div[@class="cez-business-main__news"]/div[{}]/a/span/text()'.format(i)).extract()
            item['title'] = selector.xpath('/html/body/div[@class="cez-business-main"]/div[@class="cez-business-main-wrapper cez-main-content"]/div[@class="cez-business-main__content"]/div[@class="cez-business-main__news"]/div[{}]/div[2]/h3/a/text()'.format(i)).extract()
            item['buystart_1'] = selector.xpath('/html/body/div[@class="cez-business-main"]/div[@class="cez-business-main-wrapper cez-main-content"]/div[@class="cez-business-main__content"]/div[@class="cez-business-main__news"]/div[{}]/div[3]/@buystart_1'.format(i)).extract()
            item['buyend_1'] = selector.xpath('/html/body/div[@class="cez-business-main"]/div[@class="cez-business-main-wrapper cez-main-content"]/div[@class="cez-business-main__content"]/div[@class="cez-business-main__news"]/div[{}]/div[3]/@buyend_1'.format(i)).extract()
            url_1 = 'https://www.chengezhao.com/'
            url_2 = selector.xpath('/html/body/div[@class="cez-business-main"]/div[@class="cez-business-main-wrapper cez-main-content"]/div[@class="cez-business-main__content"]/div[@class="cez-business-main__news"]/div[{}]/div[2]/h3/a/@href'.format(i)).extract()
            item['url'] = url_Splicing(url_1,url_2)
            # print(item)
            yield item
        if self.pageNum < page_Count:
            self.pageNum+=1
            url = format(self.url % self.pageNum)
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            yield request

