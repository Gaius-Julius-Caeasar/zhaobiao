# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZztenderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 开始时间
    start_time = scrapy.Field()
    # 结束时间
    end_time = scrapy.Field()
    # 跳转链接
    url = scrapy.Field()
    pass
