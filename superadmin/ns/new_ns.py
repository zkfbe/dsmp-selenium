import time
import ddddocr
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# 1、创建Chrome实例 。
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
name = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[3]/div/div/div/div/span/input')  # 账号输入框位置
name.send_keys("admin")  # 输入你的账号
pwd = driver.find_element(by=By.ID, value='password')  # 密码输入框位置
pwd.send_keys("Jtwmy@dt4gx")  # 输入你的密码
imgCode = driver.find_element(By.CLASS_NAME, "code___1wGtw")  # 验证码图片位置
code = driver.find_element(by=By.ID, value='verify_code')  # 验证码输入框位置
#time.sleep(1)
submit=driver.find_element(By.XPATH,'/html/body/div/div/div/div/form/button[1]')
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
time.sleep(2)
newns=driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/main/div/div/div[2]/div[1]/button')
newns.click()
time.sleep(1)
newns_nsname=driver.find_element(By.ID,"ns")
newns_nsname.send_keys("lzq06")
newns_admin=driver.find_element(By.ID,'username')
newns_admin.send_keys("admin")
newns_password=driver.find_element(By.ID,'password')
newns_password.send_keys("Jtwmy@dt4gx")
newns_confirmpass=driver.find_element(By.ID,'confirm_password')
newns_confirmpass.send_keys("Jtwmy@dt4gx")
modalContainer = driver.find_element(By.CLASS_NAME,"ant-modal-content")
newns_submit=modalContainer.find_element(By.XPATH,'.//div[3]/button[2]')
newns_submit.click()
time.sleep(3)  # 延迟3秒
# 4、退出访问的实例网站。
driver.quit()