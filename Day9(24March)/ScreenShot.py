import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
folder=os.path.join(os.getcwd(),'Screenshots')
os.makedirs(folder,exist_ok=True)

driver=webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()

'''
## When there is error it can be used to see where the code breaks
-> driver.save_screenshot('screenshot.png'):- screen shot of whole page
-> find that element and take screenshot of whole element
'''

# Contains can also work with attributes just use contains(@attribute,"attr_value")
driver.save_screenshot(f'{folder}/sc1.png')
sleep(3)

action=ActionChains(driver)

element=driver.find_element(By.XPATH,"(//div[@class='ADXRXN AsRsEE']/descendant::img)[3]")

action.scroll_to_element(element).perform()

element.screenshot(f'{folder}/sc2.png')
sleep(2)