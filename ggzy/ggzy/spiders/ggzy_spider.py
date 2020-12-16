import re

import scrapy
from ggzy.items import GgzyItem
from scrapy import Selector


def handle_addr(addres):
    addres = [x.strip() for x in addres]
    return addres

class GgzySpiderSpider(scrapy.Spider):
    name = 'ggzy_spider'
    allowed_domains = ['ggzy.gz.gov.cn/jyywzfcgzfcgcggg/index_1.jhtml']
    # 搜索内容
    WorkName = '智能'
    url = 'http://ggzy.gz.gov.cn/jyywzfcgzfcgcggg/index_%d.jhtml'
    # url = 'http://ggzy.gz.gov.cn/jyywzfcgzfcgcggg/index_%d.jhtml'+'?q='+WorkName

    start_urls = ['http://ggzy.gz.gov.cn/jyywzfcgzfcgcggg/index_1.jhtml'+'?q='+WorkName]
    # start_urls = ['http://ggzy.gz.gov.cn/jyywzfcgzfcgcggg/index_1.jhtml']

    # 爬取多页
    page_No = 1

    def parse(self, response):
        selector = Selector(response)
        li_list = selector.xpath('//*[@id="tab1"]/div[2]/table/tbody/tr')
        r = 1
        # 获取页数
        page_Count = response.xpath('//*[@id="tab1"]/div[2]/div[2]/div/text()').extract()
        page_Count = handle_addr(page_Count)
        page_Count = re.findall('\d*', page_Count[0])
        # print(page_Count[1])

        for i in li_list:
            item = GgzyItem()
            item['number'] = response.xpath('//*[@id="tab1"]/div[2]/table/tbody/tr[{}]/td[1]'.format(r)).xpath('string(.)').extract()
            item['title']  = response.xpath('//*[@id="tab1"]/div[2]/table/tbody/tr[{}]/td[2]'.format(r)).xpath('string(.)').extract()
            item['create_time'] = response.xpath('//*[@id="tab1"]/div[2]/table/tbody/tr[{}]/td[3]'.format(r)).xpath('string(.)').extract()
            item['url'] = response.xpath('//*[@id="tab1"]/div[2]/table/tbody/tr[{}]/td[2]/a/@href'.format(r)).extract()
            r+=1
            # print(item)
            yield item

        # 检测”下一页“按钮
        next_page = handle_addr(response.xpath('//*[@id="tab1"]/div[2]/div[2]/div/a[3]/@href').extract())
        if next_page:
            self.page_No+=1
            # print(self.page_No)
            url = format(self.url % self.page_No)
            # print(url)
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            yield request

        # 多页爬取
        # if self.page_No  < page_Count:
        #     self.page_No += 1
        #     print(self.page_No)
        #     url = format(self.url % self.page_No)
        #     request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
        #     yield request
