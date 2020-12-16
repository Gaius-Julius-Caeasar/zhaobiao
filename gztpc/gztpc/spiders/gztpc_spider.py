import scrapy
from gztpc.items import GztpcItem
from scrapy import Selector


def handle_addr(addres):
    addres = [x.strip() for x in addres]
    return addres

def int_page(page_Count):
    page_Count = [int(x) for x in page_Count]
    return page_Count

def split_selector(n_c):
    n_c = [x.split("]") for x in n_c]
    return n_c

def url_Splicing(url_1,url_2):
    url_Splicing = [url_1+x for x in url_2]
    return url_Splicing

class GztpcSpiderSpider(scrapy.Spider):
    name = 'gztpc_spider'
    # 搜索内容
    WorkName = '智能'
    allowed_domains = ['gztpc.com/tender/list?pid=4028e68133f22e130133f2a837750000&pageNo=1']
    start_urls = ['http://www.gztpc.com/tender/list?pid=4028e68133f22e130133f2a837750000&pageNo=1']
    page_No = 1
    url = 'http://www.gztpc.com/tender/list?pid=4028e68133f22e130133f2a837750000&pageNo=%d'

    def parse(self, response):
        selector = Selector(response)
        r = 1
        # 获取页数
        page_Count = selector.xpath(
            '/html/body/div[@class="contain"]/div[@class="maincontent"]/div[@class="Page"]/span[2]/text()').extract()
        page_Count = int_page(page_Count)[0]
        # print(page_Count)

        li_list = selector.xpath('/html/body/div[@class="contain"]/div[@class="maincontent"]/ul/li').extract()


        for i in li_list:
            item = GztpcItem()
            item['title'] = selector.xpath('/html/body/div[@class="contain"]/div[@class="maincontent"]/ul/li[{}]/a/text()'.format(r)).extract()
            n_c = selector.xpath('/html/body/div[@class="contain"]/div[@class="maincontent"]/ul/li[{}]/span/text()'.format(r)).extract()
            n_c = split_selector(n_c)
            item['number'] = n_c[0][0]
            item['create_time'] = n_c[0][1]
            url_2 = selector.xpath('/html/body/div[@class="contain"]/div[@class="maincontent"]/ul/li[{}]/a/@href'.format(r)).extract()
            url_1 = 'http://www.gztpc.com/'
            item['url'] = url_Splicing(url_1,url_2)
            # print(item)
            yield item
            r+=1

        if self.page_No < page_Count:
            self.page_No+=1
            url = format(self.url % self.page_No)
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            yield request



