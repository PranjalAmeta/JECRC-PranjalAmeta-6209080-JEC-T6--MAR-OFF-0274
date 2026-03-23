from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')
sleep(2)
driver.find_element(By.ID,'datepicker').send_keys('01/13/2004',Keys.ENTER)


month='Jan'
date=13

driver.find_element(By.ID,'txtDate').click()


select=Select(driver.find_element(By.CLASS_NAME,'ui-datepicker-month'))

driver.find_element()
select.select_by_visible_text(month)


sleep(4)