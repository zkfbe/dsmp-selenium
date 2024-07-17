import time
import ddddocr
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
time.sleep(1)
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
    code.send_keys(Keys.CONTROL+'a')
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
setting=driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/header[2]/div/div/div[3]/div/div/div/div[2]')
setting.click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[contains(text(),'系统管理')]").click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[1]/div/div[2]/div[2]/div[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[2]/div[2]/button').click()
time.sleep(1)
modalContainer = driver.find_element(By.CLASS_NAME,"ant-modal-content")
driver.find_element(By.XPATH,'//div[2]/form/div[1]/div/div[2]/div/div/div/div').click()
time.sleep(1)
elements=driver.find_elements(By.CLASS_NAME,"ant-select-item-option-content")
for element in elements:
    text=element.get_attribute("innerText")
    if "IAST" in text:
        element.click()
        break
driver.find_element(By.XPATH,'//div[2]/form/div[2]/div/div[2]/div/div/input').send_keys("IAST")
driver.find_element(By.XPATH,'//div[2]/form/div[3]/div/div[2]/div/div/input').send_keys("1.0.0")
time.sleep(1)
driver.find_element(By.XPATH,'//div[2]/form/div[4]/div/div[2]/div/div/div/div').click()
elements=driver.find_elements(By.CLASS_NAME,"ant-select-item-option-content")
time.sleep(1)
for element in elements:
    if element.get_attribute("innerText") == "HTTPS":
        element.click()
        break
driver.find_element(By.XPATH,'//div[2]/form/div[5]/div/div[2]/div/div/input').send_keys("192.168.121.200")
driver.find_element(By.XPATH,'//div[2]/form/div[6]/div/div[2]/div/div/div/div[2]/input').send_keys("443")
driver.find_element(By.XPATH,'//div[2]/form/div[7]/div/div[2]/div/div/input').send_keys("6675395b47811d2b7c7a8c73")
driver.find_element(By.XPATH,'//div[2]/form/div[8]/div/div[2]/div/div/input').send_keys("209f2cbc-440e-4bec-a419-4ad3b441c6f2")
driver.find_element(By.XPATH,'//div[2]/form/div[9]/div/div/div/div/div/button[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//div[2]/form/div[9]/div/div/div/div/div/button[3]').click()
time.sleep(3)
# 4、退出访问的实例网站。
driver.quit()