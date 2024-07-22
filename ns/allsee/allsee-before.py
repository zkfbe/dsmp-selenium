import time
import pymongo
import ddddocr
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import sys
import os

os.remove('1.txt')
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
sys.stdout = Logger('1.txt')
user = 'root'
pwd = 'Yg3y!LzmEG9oXqrp'
host = '192.168.142.200'
port = '27017'
uri = "mongodb://%s:%s@%s" % (user, pwd, host + ":" + port + "/" )
client = MongoClient(uri)
mydb=client['db_dp_vuln']
tbl_vuln=mydb['tbl_vuln']
number1=tbl_vuln.aggregate([
{"$match":{"ns":"lzq3","vuln_status_locate":{'$ne':2}}},
{"$group":{"_id":"$risk_level","count":{'$sum':1}}},
{"$sort":{"_id":-1}}
])
number2=tbl_vuln.aggregate([
{"$match":{"ns":"lzq3"}},
{"$group":{"_id":"$risk_level","count":{"$sum":1}}},
{"$sort":{"_id":-1}}
])
number3=tbl_vuln.aggregate([
{"$match":{"ns":"lzq3","vuln_status_locate":{"$ne":2}}},
{"$group":{"_id":"$vuln_type","count":{"$sum":1}}},
{"$sort":{"count":-1}},
{"$limit":10}
])
number4=tbl_vuln.aggregate([
{"$match":{"ns":"lzq3"}},
{"$group":{"_id":"$vuln_type","count":{"$sum":1}}},
{"$sort":{"count":-1}},
{"$limit":10}
])
number5=tbl_vuln.aggregate([
{"$match":{"ns":"lzq3","vuln_status_locate":2}},
{"$group":{"_id":"$ns","count":{"$sum":1}}}
])
number6=tbl_vuln.aggregate([
{"$match":{"ns":"lzq3","vuln_status_locate":{"$ne":2}}},
{"$group":{"_id":"$ns","count":{"$sum":1}}}
])
print("漏洞风险分布:")
print('未闭环:')
list1=list(number1)
print("严重:",end='')
print(list1[0].get('count'))
print("高危:",end='')
print(list1[1].get('count'))
print("中危:",end='')
print(list1[2].get('count'))
print("低危:",end='')
print(list1[3].get('count'))
print("安全:",end='')
print(list1[4].get('count'))
print()
print('全部:')
list2=list(number2)
print("严重:",end='')
print(list2[0].get('count'))
print("高危:",end='')
print(list2[1].get('count'))
print("中危:",end='')
print(list2[2].get('count'))
print("低危:",end='')
print(list2[3].get('count'))
print("安全:",end='')
print(list2[4].get('count'))
print()
print("漏洞类型TOP10:")
print('未闭环:')
list3=list(number3)
print(list3[0].get('_id'),end=' ')
print(list3[0].get('count'))
print(list3[1].get('_id'),end=' ')
print(list3[1].get('count'))
print(list3[2].get('_id'),end=' ')
print(list3[2].get('count'))
print(list3[3].get('_id'),end=' ')
print(list3[3].get('count'))
print(list3[4].get('_id'),end=' ')
print(list3[4].get('count'))
print(list3[5].get('_id'),end=' ')
print(list3[5].get('count'))
print(list3[6].get('_id'),end=' ')
print(list3[6].get('count'))
print(list3[7].get('_id'),end=' ')
print(list3[7].get('count'))
print(list3[8].get('_id'),end=' ')
print(list3[8].get('count'))
print(list3[9].get('_id'),end=' ')
print(list3[9].get('count'))
print()
print('全部:')
list4=list(number4)
print(list4[0].get('_id'),end=' ')
print(list4[0].get('count'))
print(list4[1].get('_id'),end=' ')
print(list4[1].get('count'))
print(list4[2].get('_id'),end=' ')
print(list4[2].get('count'))
print(list4[3].get('_id'),end=' ')
print(list4[3].get('count'))
print(list4[4].get('_id'),end=' ')
print(list4[4].get('count'))
print(list4[5].get('_id'),end=' ')
print(list4[5].get('count'))
print(list4[6].get('_id'),end=' ')
print(list4[6].get('count'))
print(list4[7].get('_id'),end=' ')
print(list4[7].get('count'))
print(list4[8].get('_id'),end=' ')
print(list4[8].get('count'))
print(list4[9].get('_id'),end=' ')
print(list4[9].get('count'))
print()
print('漏洞状态分布:')
print()
print('漏洞闭环情况:')
print('闭环:')
list5=list(number5)
list5number=0
if list5:
    list5number=list5[0].get('count')
print(list5number)
print('未闭环:')
list6=list(number6)
list6number=0
if list6:
    list6number=list6[0].get('count')
print(list6number)
print('闭环率:')
if list5number+list6number==0:
    print(0)
else:
    print(round((list5number/(list5number+list6number)*100),1),end='%')