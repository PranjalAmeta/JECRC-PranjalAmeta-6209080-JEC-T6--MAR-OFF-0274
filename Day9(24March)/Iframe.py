'''
Iframes are in lamen terms nested html
iFrames (Inline Frames) are HTML elements used to embed another webpage inside a webpage.
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)
#
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("hello") # wont work
# # bcoz the control in the outer html page
# sleep(3)


# iframe=driver.find_element(By.ID,'singleframe')
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("hello")
# sleep(2)


driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()
first_iframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(first_iframe)

nested_frame=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(nested_frame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("ky bolti public")
sleep(3)

driver.switch_to.parent_frame() # switches to parent frame
driver.switch_to.default_content() # switches to main/default page
