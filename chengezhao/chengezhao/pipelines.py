# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter


class ChengezhaoPipeline:
    def open_spider(self, spider):
        print("Chengezhao-Csv.opend")
        try:
            self.csvFile = open("recruit.csv", "w+", encoding='utf-8')
            self.writer = csv.writer(self.csvFile)
            self.writer.writerow(('截止时间', '项目标题', '开始时间', '结束时间', '跳转链接'))
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
        print("Chengezhao-Csv closed")
        print("Chengezhao-Csv总共爬取", self.count, "份资料")

    def process_item(self, item, spider):
        try:
            # 在控制台显示出写入数据的内容
            # print(item)
            # 这里会出现控制台有读取可未写入csv中的情况,可能是csv在前面运行过程中不小心关闭了导致无法写入内容
            if self.opened:
                # 写入CSV文件
                self.writer.writerow((item['create_time'], item['title'], item['buystart_1'], item['buyend_1'], item['url']))
                self.count += 1
        except Exception as err:
            print(err)
        return item
