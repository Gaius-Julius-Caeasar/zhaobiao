import os
import threading

from scrapy import cmdline


def csv_1():
    os.chdir('F:/zhaobiao/caigou/caigou')
    os.system("scrapy crawl Caigou --nolog")
def csv_2():
    os.chdir('F:/zhaobiao/chengezhao/chengezhao')
    os.system("scrapy crawl Chengezhao --nolog")
def csv_3():
    os.chdir('F:/zhaobiao/ebidding/ebidding')
    os.system("scrapy crawl ebidding_spider --nolog")
def csv_4():
    os.chdir('F:/zhaobiao/ggzy/ggzy')
    os.system("scrapy crawl ggzy_spider --nolog")
def csv_5():
    os.chdir('F:/zhaobiao/gzqunsheng/gzqunsheng')
    os.system("scrapy crawl gzqunsheng_spider --nolog")
def csv_6():
    os.chdir('F:/zhaobiao/gztpc/gztpc')
    os.system("scrapy crawl gztpc_spider --nolog")
def csv_7():
    os.chdir('F:/zhaobiao/zztender/zztender')
    os.system("scrapy crawl zztender_spider --nolog")

if __name__ == '__main__':
    threads = [threading.Thread(target=csv_1),
               threading.Thread(target=csv_2),
               threading.Thread(target=csv_3),
               threading.Thread(target=csv_4),
               threading.Thread(target=csv_5),
               threading.Thread(target=csv_6),
               threading.Thread(target=csv_4)]
    for t in threads:
        # 启动线程
        t.start()
