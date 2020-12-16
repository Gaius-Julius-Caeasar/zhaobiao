import re
import scrapy
from scrapy import Selector
from caigou.items import CaigouItem


def handle_addr(addres):
    addres = [x.strip() for x in addres]
    return addres

def split_selector(n_c):
    n_c = [x.split(",") for x in n_c]
    return n_c

def Name_text(Name, url_2=None):
    if Name == ['招标公告']:
        url_2 = 'tenderannouncement/viewHome.do'
    elif Name == ['单一来源采购公示']:
        url_2 = 'purchaseannouncebasic/viewHome.do'
    elif Name == ['比选公告']:
        url_2 = 'tenderannouncement/viewCompare.do'
    elif Name == ['询价公告']:
        url_2 = 'enquiry/viewForAd.do'
    # 尚未补全
    elif Name == ['竞争性谈判文件']:
        url_2 = '123456'
    return url_2

class CaigouSpider(scrapy.Spider):
    name = 'Caigou' #定义爬虫名称
    allowed_domains = ['caigou.chinatelecom.com.cn/MSS-PORTAL/announcementjoin/list.do?provinceJT=JT']  #定义爬虫域
    start_urls = ['https://caigou.chinatelecom.com.cn/MSS-PORTAL/announcementjoin/list.do?provinceJT=JT&paging.start=1']# 定义开始爬虫链接

    # 爬取多页
    pageNum = 1
    url = 'https://caigou.chinatelecom.com.cn/MSS-PORTAL/announcementjoin/list.do?provinceJT=JT&paging.start=%d'

    def parse(self, response): #撰写爬虫逻辑
        # 获取到页数
        selector = Selector(response)
        # page = selector.xpath('//*[@id="two_pages_all"]//div[1]//div[2]//table[4]//tr//td[8]').xpath('string(.)').extract()
        # page = int(re.sub("\D",'',str(page)))
        # page = page/10
        # if page%10>0:
        #     page = int(page+1)
        # else:
        #     page = int(page)
        #  t(page) # 打印页数

        # 行数获取
        li_list = selector.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr').xpath('string(.)').extract()
        r = 1
        for i in li_list:
            url_1 = response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[3]/a/@onclick'.format(r)).extract()
            if len(url_1) == 1:
                # 初始化容器
                item = CaigouItem()
                # 省份
                item['province'] = response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[1]'.format(r)).xpath('string(.)').extract()
                # 是否终止
                item['end'] = handle_addr(response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[2]'.format(r)).xpath('string(.)').extract())
                # 公司名称
                item['type'] = handle_addr(response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[3]'.format(r)).xpath('string(.)').extract())
                # 公告类型
                item['Name'] = handle_addr(response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[4]'.format(r)).xpath('string(.)').extract())
                 # 创建时间日期
                item['create_time'] = handle_addr(response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[6]'.format(r)).xpath('string(.)').extract())
                # 开始时间
                item['start_time'] = response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[7]'.format(r)).xpath('string(.)').extract()
                # 截止时间
                item['end_time'] =  response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[8]'.format(r)).xpath('string(.)').extract()

                # 获取到目标的url
                Name = handle_addr(
                    response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[3]/tr[{}]/td[5]'.format(r)).xpath(
                        'string(.)').extract())
                url_2 = Name_text(Name)
                url_3 = url_1[0].split(',')[2][1:33]
                url_4 = url_1[0].split(',')[0][6:13]
                item['url'] = 'https://caigou.chinatelecom.com.cn/MSS-PORTAL/'+str(url_2)+'?encryCode='+str(url_3)+'&id='+str(url_4)

                yield item
            r+=1

        # 检测”下一页“按钮
        next_page = handle_addr(response.xpath('//*[@id="two_pages_all"]/div[1]/div[2]/table[4]/tr/td[10]/a[1]').extract())
        if next_page:
            self.pageNum+=10
            url = format(self.url % self.pageNum)
            request = scrapy.Request(url = url,callback=self.parse,dont_filter=True)
            yield request



