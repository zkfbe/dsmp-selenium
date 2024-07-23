import time
import random

import ddddocr
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
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
    code.send_keys(Keys.COMMAND + 'a')
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
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/header[2]/div/div/div[2]/ul/li[2]/span/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div/div[1]/div/div/button[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/form/div[1]/div/div[2]/div/div/span/input').send_keys("project-"+''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4)))
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/form/div[2]/div/div[2]/div/div/div/div/span[1]/input').click()
time.sleep(1)
elements=driver.find_elements(By.CLASS_NAME, 'ant-cascader-menu-item-content')
for element in elements:
        element.get_attribute('innerText')=="lzq3"
        element.click()
        break
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/form/div[3]/div/div[2]/div/div/div/div/span[1]/input').click()
time.sleep(1)
elements=driver.find_elements(By.CLASS_NAME, 'ant-select-item-option-content')
for element in elements:
    if element.get_attribute("innerText") == "admin":
        element.click()
        break
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/form/div[4]/div/div[2]/div/div/div/textarea').send_keys('项目描述')
time.sleep(1)
driver.find_element(By.XPATH,'//form/div[5]/div/div[2]/div/div/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//div[2]/table/tbody/tr[3]/td[1]/label/span/input').click()
driver.find_element(By.XPATH,'//div[2]/table/tbody/tr[4]/td[1]/label/span/input').click()
driver.find_element(By.XPATH,'//div[2]/table/tbody/tr[5]/td[1]/label/span/input').click()
driver.find_element(By.XPATH,'//div[2]/table/tbody/tr[6]/td[1]/label/span/input').click()
driver.find_element(By.XPATH,'//div[2]/table/tbody/tr[7]/td[1]/label/span/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//div[2]/div/div[2]/div[3]/button[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/form/div[6]/div/div[2]/div/div/span/input').send_keys("1.1.0")
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/form/div[9]/div/div[2]/div/div/div/textarea').send_keys('版本描述')
time.sleep(6)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/form/div[10]/button[1]').click()
time.sleep(1)
# 4、退出访问的实例网站。
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//div/div/ul/li[2]/span/div').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div[2]/div/div/div[1]/button').click()
time.sleep(1)
name=driver.find_element(By.XPATH,'//div[2]/form/div[1]/div/div[2]/div/div/span/input')
name.send_keys(Keys.COMMAND + 'a')
name.send_keys(Keys.BACKSPACE)
name.send_keys('project-'+''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4)))
time.sleep(1)
driver.find_element(By.XPATH,'//div[3]/div/div/div[3]/div/button[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//main/div[2]/div/div/div[5]/div/div/div[1]/div[2]/div/div/button').click()
time.sleep(1)
number=driver.find_element(By.ID,'version_name')
number.send_keys('1.2.0')
time.sleep(4)
driver.find_element(By.XPATH,'//div/div[3]/div/div/div[3]/div/button[2]').click()
driver.find_element(By.XPATH,'//div/header[2]/div/div/div[2]/ul/li[2]/span/a').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[2]/div/div[1]/div[1]/div[2]/button[1]')
# 4、退出访问的实例网站。
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/button').click()
time.sleep(1)
driver.find_element(By.ID,'tag').send_keys('222')
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='tag']/../../../../../../../../../../div[2]/button[2]").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#root > div > section > div > main > div > div.ant-spin-nested-loading > div > div.card_item___3N9w4.ms-main > div.card_item_footer___1v4LL > div:nth-child(1) > div.ms-tips.card_item_tag___3Nchg > div > div > div:nth-child(1) > svg ').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div/div/ul/li[1]/span/div').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div').click()
time.sleep(2)
driver.find_element(By.XPATH,'//main/div/div[2]/div/div[1]/div[1]/div[2]/button[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//main/div/div/div[2]/div[1]/div[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//main/div/div/div[2]/div[2]/div/div[1]/div[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//main/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/button').click()
time.sleep(3)
# 4、退出访问的实例网站。
driver.quit()