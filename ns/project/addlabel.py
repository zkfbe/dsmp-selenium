import time
import ddddocr
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import action_chains
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
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/header[2]/div/div/div[2]/ul/li[2]/span/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/button').click()
time.sleep(1)
driver.find_element(By.ID,'tag').send_keys('222')
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='tag']/../../../../../../../../../../div[2]/button[2]").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#root > div > section > div > main > div > div.ant-spin-nested-loading > div > div.card_item___3N9w4.ms-main > div.card_item_footer___1v4LL > div:nth-child(1) > div.ms-tips.card_item_tag___3Nchg > div > div > div:nth-child(1) > svg ').click()
time.sleep(3)
driver.quit()