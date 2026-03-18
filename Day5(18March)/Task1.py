from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()
'''
driver.get('https://the-internet.herokuapp.com/')
sleep(4)

check_box=driver.find_element(By.LINK_TEXT,"Checkboxes")
print('check_box found')

drag_drop=driver.find_element(By.PARTIAL_LINK_TEXT,'Drag and Drop')
print('drag_drop found')

li_count=driver.find_elements(By.TAG_NAME,'li')
print('li count is:',len(li_count))
'''

driver.get('https://the-internet.herokuapp.com/tables')
sleep(4)
email_find=driver.find_element(By.XPATH,"//table[@id='table1']/descendant::td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
print('email_find found')

del_link=driver.find_element(By.XPATH,"//table[@id='table1']/descendant::td[text()='Bach']/following-sibling::td[5]/a[2]")
print('del_link found')

table_two=driver.find_element(By.XPATH,"//table[2]")
print('table_two found')

parent_found=driver.find_element(By.XPATH,"//table[@id='table2']/descendant::td[text()='$100.00']/parent::tr")
print('parent_found')

driver.quit()