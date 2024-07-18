import time
import pymongo
import ddddocr
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

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
print(list(number1))
print('全部:')
print(list(number2))
print()
print("漏洞类型TOP10:")
print('未闭环:')
print(list(number3))
print('全部:')
print(list(number4))
print()
print('漏洞状态分布:')
print('漏洞闭环情况:')
print('闭环:')
number5count=0
if list(number5):
    number5count=list(number5)[0].get('count')
print(number5count)
print('未闭环:')
number6count=0
if list(number6):
    number6count=list(number6)[0].get('count')
print(number6count)
print('闭环率:')
print(number5count/number6count*100+"%")
# 1、创建Chrome实例 。
driver = webdriver.Chrome()
# 2、driver.get方法将定位在给定的URL的网页 。
driver.get("https://192.168.142.200")  # get接受url可以是如何网址，此处以百度为例
driver.maximize_window()
dd1 = driver.find_element(by=By.ID, value='details-button')
dd1.click()
dd2 = driver.find_element(by=By.ID, value='proceed-link')
dd2.click()
time.sleep(2)
nsadmin=driver.find_element(By.XPATH,'/html/body/div/div/div/div/form/button[2]')
nsadmin.click()
nsname=driver.find_element(By.XPATH,'/html/body/div/div/div/div/form/div[3]/div/div/div/div/span/input')
nsname.send_keys('lzq3')
next=driver.find_element(By.XPATH,'/html/body/div/div/div/div/form/button[1]')
next.click()
name = driver.find_element(By.ID, 'username')  # 账号输入框位置
name.send_keys("admin")  # 输入你的账号
pwd = driver.find_element(by=By.ID, value='password')  # 密码输入框位置
pwd.send_keys("Jtwmy@dt4gx")  # 输入你的密码
imgCode = driver.find_element(By.CLASS_NAME, "code___1wGtw")  # 验证码图片位置
code = driver.find_element(by=By.ID, value='verify_code')  # 验证码输入框位置
submit=driver.find_element(By.XPATH,'/html/body/div/div/div/div/form/div[2]/button[2]')
# 以下为识别验证码的代码
while(driver.current_url=="https://192.168.142.200/login"):
    code.send_keys(Keys.CONTROL + 'a')
    code.send_keys(Keys.BACKSPACE)
    imgCode.screenshot("code.png")  # 将验证码截图，保存为code.png
    ocr = ddddocr.DdddOcr()
    with open("code.png", "rb") as fp:
        image = fp.read()
    catch = ocr.classification(image)  # 验证码返回给catch
    code.send_keys(catch)  # 将识别到的验证码输入到框内
    submit.click()
    imgCode.click()
    time.sleep(1)

time.sleep(3)

# 4、退出访问的实例网站。
driver.quit()