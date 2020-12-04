
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv

import bs4
import requests
url="https://main.sci.gov.in/case-status"
res=requests.get(url)
bs=bs4.BeautifulSoup(res.text,'html.parser')

PATH = "C:/Users/ymaha/Downloads/chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://main.sci.gov.in/case-status")


captcha_read = driver.find_element_by_id("cap").text
# print(captcha_read)

captcha = driver.find_element_by_name("ansCaptcha")
captcha.send_keys(captcha_read.strip())

diaryNo = driver.find_element_by_name("CaseDiaryNumber")
diaryNo.send_keys(1)

year = driver.find_element_by_id("CaseDiaryYear")
drpdwn = Select(year)
drpdwn.select_by_visible_text('2019')

driver.find_element_by_id("getCaseDiary").click()



tableData = driver.find_elements_by_xpath("//*[@id='collapse1']/div/table")
with open('scarpdata.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for row in tableData.find_elements_by_xpath("//*[@id='collapse1']/div/table/tbody/tr"):
        wr.writerow([d.text for d in row.find_elements_by_xpath("//*[@id='collapse1']/div/table/tbody/tr[1]/td")])
