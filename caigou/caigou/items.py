# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaigouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field() # 省份
    end = scrapy.Field() # 是否终止
    Name = scrapy.Field() # 公司名称
    code = scrapy.Field() # 公告编码
    type = scrapy.Field() # 公告类型
    create_time = scrapy.Field() # 创建时间日期
    start_time = scrapy.Field() # 开始时间
    end_time = scrapy.Field() # 截止时间
    url = scrapy.Field() # 跳转链接