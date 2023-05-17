# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:22:26 2023

@author: Wantzu
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.feastogether.com.tw/booking/Sunrise'

driver = webdriver.Chrome('chromedriver')
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()


#關閉公告頁面
X = driver.find_element(By.CLASS_NAME, 'css-ywgpzb')
X.click()

#會員登入
login = driver.find_element(By.CLASS_NAME, 'fStTgo')
login.click()

phone = driver.find_element(By.NAME, 'phoneNumber')
phone.send_keys('09XXXXX')#這邊需輸入電話

pwd = driver.find_element(By.NAME, 'password')
pwd.send_keys('XXXXX')#這邊需輸入密碼

OK = driver.find_element(By.CLASS_NAME, 'login')
OK.click()
time.sleep(3)

#下拉選單畫布
svg = driver.find_elements(By.CLASS_NAME, 'css-1q69m9j')
svg[0].click() #店別

#點選店別
area = driver.find_element(By.CLASS_NAME, 'frLmcK')
area.click() 


svg[1].click() #成員
num = driver.find_elements(By.CLASS_NAME, 'hjjfwZ')
for i in range(2): #這邊代表2位成人，如需8人就改成range(8)
    num[0].click()


timesvg = driver.find_elements(By.CLASS_NAME, 'css-33zf0e')
timesvg[0].click()
time.sleep(1)

time1 = driver.find_elements(By.CLASS_NAME, 'css-1tla7oo')
time1[2].click() #午餐、下午餐、晚餐
time.sleep(1)

datesvg = driver.find_elements(By.CLASS_NAME, 'css-2gu9x4')
datesvg[2].click()

date1 = driver.find_elements(By.CLASS_NAME, 'react-datepicker__day--0' + str(15))#這邊是日期，輸入要搶的日期，今天5/16，0點要搶6/17號的，這邊就改成17
date1[1].click()

search = driver.find_element(By.CLASS_NAME, 'ijfYSV')
search.click()
time.sleep(2)

btndiv = driver.find_element(By.CLASS_NAME, 'bLsuFy')
btns = btndiv.find_elements(By.TAG_NAME, 'button')
btns[0].click()
time.sleep(10)

send = btns[len(btns) - 1]
print(send.text)
send.click()
time.sleep(2)


html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
html.send_keys(Keys.END)
time.sleep(1)

agree = driver.find_element(By.CLASS_NAME, 'PrivateSwitchBase-input')   
agree.click()

booking = driver.find_element(By.CLASS_NAME, 'sendValidBooking')
booking.click()
print(booking.text)
        

