'''
Drop down are generally in select tab

# 3 ways to select the options
1) by visible text
2) by index
3) by value attribute
'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
# sleep(3)
# country_dropdown=driver.find_element(By.ID,'country')
# # find_element() as we are selecting one whole dropdown
# dropdown=Select(country_dropdown)
# # 3rd way
# dropdown.select_by_value('india')
# # 2nd way
# dropdown.select_by_index(9)           # 0 based index
# # 1st way
# dropdown.select_by_visible_text('Australia')
# sleep(3)



''' ---------- Real time Appliction ---------- '''

# driver.get('https://www.lenskart.com')
# driver.maximize_window()
# sleep(4)
# search_field=driver.find_element(By.ID,"autocomplete-0-input")
# search_field.send_keys('sunglasses',Keys.ENTER)
# sleep(4)
# type_drop=driver.find_element(By.ID,'sortByDropdown')
# dropdown=Select(type_drop)
# dropdown.select_by_value('created')
# sleep(4)
# search_first=driver.find_element(By.XPATH,"//div[@class='sc-bf32d8a7-0 gOVKHN']/descendant::div[1]")
# search_first.click()
# sleep(4)