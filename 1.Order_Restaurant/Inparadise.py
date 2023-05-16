# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:48:51 2023

@author: Wantzu
"""

import time,datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.feastogether.com.tw/booking/Inparadise'

driver = webdriver.Chrome('chromedriver')
driver.get(url)
driver.implicitly_wait(3)
driver.maximize_window()

'''
for i in range(1000):
    time.sleep(3)
    driver.refresh()
    if time.now().isoformat() == '12:15:00':
        break
'''

#關閉公告頁面
X = driver.find_element(By.CLASS_NAME, 'css-ywgpzb')
X.click()

#會員登入
login = driver.find_element(By.CLASS_NAME, 'fStTgo')
login.click()

phone = driver.find_element(By.NAME, 'phoneNumber')
phone.send_keys('0975226621')

pwd = driver.find_element(By.NAME, 'password')
pwd.send_keys('ji394su3')

OK = driver.find_element(By.CLASS_NAME, 'login')
OK.click()
time.sleep(1)

#下拉選單畫布
svg = driver.find_elements(By.CLASS_NAME, 'css-1q69m9j')
svg[0].click() #店別

#點選店別
area = driver.find_elements(By.CLASS_NAME, 'frLmcK')
area[1].click() #0是微風店、1是新莊店


svg[1].click() #成員
num = driver.find_elements(By.CLASS_NAME, 'dsDilA')
for i in range(8):
    num[0].click()


timesvg = driver.find_elements(By.CLASS_NAME, 'css-33zf0e')
timesvg[0].click()
time.sleep(1)

time1 = driver.find_elements(By.CLASS_NAME, 'css-50viod')
time1[1].click() #午餐、下午餐、晚餐
time.sleep(1)

datesvg = driver.find_elements(By.CLASS_NAME, 'css-srhau5')
datesvg[2].click()

date1 = driver.find_elements(By.CLASS_NAME, 'react-datepicker__day--0' + str(12))
date1[1].click()
 
search = driver.find_element(By.CLASS_NAME, 'searchBooking')
search.click()
print(search.text)
time.sleep(1)

isee = driver.find_elements(By.CLASS_NAME, 'QlVA-D')
isee[1].click()


btndiv = driver.find_element(By.CLASS_NAME, 'bLsuFy')
btns = btndiv.find_elements(By.TAG_NAME, 'button')
btns[0].click()

#驗證碼區塊
code = driver.find_element(By.NAME, 'captchValue')


send = btns[len(btns) - 1]
print(send.text)
send.click()
time.sleep(1)

iseediv = driver.find_element(By.CLASS_NAME, 'hQEXJm')
iseediv.find_element(By.TAG_NAME, 'button').click()
time.sleep(1)

html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
html.send_keys(Keys.END)
time.sleep(1)

agree = driver.find_element(By.CLASS_NAME, 'PrivateSwitchBase-input')   
agree.click()

booking = driver.find_element(By.CLASS_NAME, 'sendValidBooking')
booking.click()
print(booking.text)
        

