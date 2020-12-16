
import scrapy
from gzqunsheng.items import GzqunshengItem
from scrapy import Selector




def handle_addr(addres):
    addres = [x.strip() for x in addres]
    return addres

def url_Splicing(url_1,url_2):
    url_Splicing = [url_1+x for x in url_2]
    return url_Splicing

class GzqunshengSpiderSpider(scrapy.Spider):
    name = 'gzqunsheng_spider'
    allowed_domains = ['gzqunsheng.com/info2.php?CateId=1']
    start_urls = ['http://gzqunsheng.com/info2.php?CateId=1&page=1']
    page_No = 1
    url = 'http://gzqunsheng.com/info2.php?CateId=1&page=%d'

    def parse(self, response):
        selector = Selector(response)
        # 获取页数
        page_Count = selector.xpath('//*[@id="turn_page"]/a/text()').extract()[-3]
        page_Count = int(page_Count)
        # print(page_Count)

        li_list = selector.xpath('//*[@id="zb_notice_tab"]/tbody/tr').extract()
        r=1
        for i in li_list:
            item = GzqunshengItem()
            item['title'] = handle_addr(selector.xpath('//*[@id="zb_notice_tab"]/tbody/tr[{}]/td[1]/a'.format(r)).xpath('string(.)').extract())
            item['number'] = selector.xpath('//*[@id="zb_notice_tab"]/tbody/tr[{}]/td[2]'.format(r)).xpath('string(.)').extract()
            item['create_time'] = selector.xpath('//*[@id="zb_notice_tab"]/tbody/tr[{}]/td[3]'.format(r)).xpath('string(.)').extract()
            url_2 = selector.xpath('//*[@id="zb_notice_tab"]/tbody/tr[{}]/td[1]/a/@href'.format(r)).extract()
            url_1= 'http://www.gzqunsheng.com/'
            item['url'] = url_Splicing(url_1,url_2)
            # print(item)
            yield item
            r+=1


        if self.page_No < page_Count:
            self.page_No += 1
            # print(self.page_No)
            url = format(self.url % self.page_No)
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            yield request