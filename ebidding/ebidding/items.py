# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EbiddingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    number = scrapy.Field()
    # url 链接
    url = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 发布日期
    create_time = scrapy.Field()
    pass
