# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class CaigouPipeline(object):
    def open_spider(self, spider):
        print("Caigou—Csv.opend")
        try:
            self.csvFile = open("recruit.csv", "w+", encoding='utf-8')
            self.writer = csv.writer(self.csvFile)
            self.writer.writerow(('省份', '终止', '公告编码', '公告名称', '创建时间日期', '开始时间','截止时间', '跳转链接'))
            self.opened = True
            self.count = 0
        except Exception as err:
            print(err)
            self.opened = False
            # 运行结束后关闭并总结爬取数据内容

    def close_spider(self, spider):
        # 询问后台csv通道是否开启
        if self.opened:
            # 如果是开启状态就关闭他
            self.csvFile.close()
            self.opened = False
        print("Caigou-Csv closed")
        print("Caigou-Csv总共爬取", self.count, "份资料")

    def process_item(self, item, spider):
        try:
            # 在控制台显示出写入数据的内容
            # print(item)
            # 这里会出现控制台有读取可未写入csv中的情况,可能是csv在前面运行过程中不小心关闭了导致无法写入内容
            if self.opened:
                # 写入CSV文件
                self.writer.writerow((item['province'], item['end'], item['Name'], item['type'], item['create_time'],
                                      item['start_time'], item['end_time'], item['url']))
                self.count += 1
        except Exception as err:
            print(err)
        return item



