# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChengezhaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 发布日期
    create_time = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 状态
    state = scrapy.Field()
    # 开始时间
    buystart_1 = scrapy.Field()
    # 结束时间
    buyend_1 = scrapy.Field()
    # 跳转链接
    url = scrapy.Field()
    pass
