'''
-> Alerts are in the form of pop-up
-> Alerts are of three types
1) simple alerts :- displays a message and with ok and cancel button
2) confirm alerts :-
3) prompt alerts  :-
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

'''# Simple Alert
simple_alert=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
sleep(2)
simple_alert.click()
alert=driver.switch_to.alert        # it will switch to alert
alert.accept()
sleep(2)

# confirm alert
confirm_alert=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
confirm_alert.click()
sleep(4)
alert=driver.switch_to.alert
# alert.accept()
alert.dismiss()
sleep(5)

# Prompt alert
prompt_alert=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
prompt_alert.click()
sleep(3)
alert=driver.switch_to.alert
alert.send_keys('ky bolti public')
alert.accept()
sleep(2)
'''

wait=WebDriverWait(driver,10)
simple_alert=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
alert=wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
# alert.dismiss()
sleep(2)







