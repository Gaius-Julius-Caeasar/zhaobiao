import datetime
import os
from multiprocessing import Pool

def csv_create(name,spider):
    os.chdir('./{}/{}'.format(name,name))
    os.system("scrapy crawl {} --nolog".format(spider))

def csv_creates(z):
    return csv_create(z[0],z[1])

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    print(starttime)
    li_list = [('caigou','Caigou'),('chengezhao','Chengezhao'),('ebidding','ebidding_spider'),
               ('ggzy','ggzy_spider'),('gzqunsheng','gzqunsheng_spider'),('gztpc','gztpc_spider'),
               ('zztender','zztender_spider')]
    with Pool(7) as p:
        p.map(csv_creates,li_list)
        endtime1 = datetime.datetime.now()
        print((endtime1 - starttime).seconds)
    p.close()

    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)