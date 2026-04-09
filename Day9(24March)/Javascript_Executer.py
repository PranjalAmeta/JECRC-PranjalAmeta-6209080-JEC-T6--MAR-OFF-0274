'''
By action chains we move with front end
by js_executor we move with backend element
when front end / UI doesnt work properly then we will use the backend part
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(2)
# to the bottom
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)

# Back to top
driver.execute_script('window.scrollTo(0,0);')
sleep(2)

# using scroll by
driver.execute_script('window.scrollTo(0,500)')  # Scroll down by 500px
sleep(5)
driver.execute_script('window.scrollBy(0,-500);')  # scrolling up 500px can use negative in by
sleep(2)

# Scrolling to elements
element=driver.find_element(By.XPATH,"(//div[@class='ADXRXN AsRsEE']/descendant::img)[3]")
driver.execute_script('arguments[0].scrollIntoView();',element)
sleep(3)

# clicking
click_ele=driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')
driver.execute_script('arguments[0].click();',click_ele)
sleep(3)




# For scroll to and scroll by we use :- window
# for all others we use :- arguments[0]