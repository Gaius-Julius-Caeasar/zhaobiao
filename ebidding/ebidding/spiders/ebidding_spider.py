import json

import scrapy
from scrapy import Selector

from ebidding.items import EbiddingItem


class EbiddingSpiderSpider(scrapy.Spider):
    name = 'ebidding_spider'
    allowed_domains = ['ebidding.com/portal/html/index.html#page=main:announcement']
    json_url = '/ebd?type=&df=&department=&industry=&bidType=&guanjianzi=&openMode=&showDateSort=1&platformType=&_=1607500341234&on=false&page='
    start_urls = ['http://www.ebidding.com/portal/announcement'+json_url+'1']

    url = 'http://www.ebidding.com/portal/announcement'+json_url+'%d'

    page_No = 1

    def parse(self, response):
        # print(response)

        item = EbiddingItem()
        rs = json.loads(response.text)
        data = rs.get('result').get('content')
        # 获取页数
        page_Count = rs.get('result').get('totalPages')
        # print(page_Count)

        for dz in data:
            item['number'] = dz.get('code')
            item['title'] = dz.get('title')
            item['create_time'] = dz.get('showDate')
            item['url'] = 'http://www.ebidding.com/portal/html/index.html#page=main:notice_details?'+"tenderType=" + str(dz.get('tenderType')) + "&" +"etId=" + str(dz.get('etId')) + "&" +"type=" + str(dz.get('type')) + "&" +"htmlContentId=" + str(dz.get('htmlContentId')) + "&" +"platform=" + str(dz.get('platformType'))
            # print(item)
            yield item

        if self.page_No < page_Count:
            self.page_No += 1
            # print(self.page_No)
            url = format(self.url % self.page_No)
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            yield request
