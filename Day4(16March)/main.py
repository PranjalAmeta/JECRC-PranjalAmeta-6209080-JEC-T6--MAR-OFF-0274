from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)

# driver.get('https://testautomationpractice.blogspot.com/')


'''
- send_keys sends data to a particular text field
- clear():- clears the data in a text field 
- get_attribute() in Selenium is used to read the value 
of an HTML attribute from a web element.
- click():- clicks a particular search button
'''
# name=driver.find_element(By.ID,"name")
# name.send_keys("Pranjal Ameta")
# sleep(2)
# name.clear()
# email=driver.find_element(By.XPATH,"//input[@id='email']")
# email.send_keys("abc@gmai.com")
# email.clear()
# sleep(2)
#
# print(name.get_attribute("value"))
#
# driver.get('https://www.amazon.com')
# sleep(5)
# search_text=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
# search_text.clear()
# search_text.send_keys("asus rog")
# search_button=driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']")
# search_button.click()

''' Simpler way to do this '''
# search_text=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
# search_text.clear()
# search_text.send_keys("asus rog",Keys.ENTER)


''' For radio button '''
# driver.get('https://testautomationpractice.blogspot.com/')
# radio_button=driver.find_element(By.XPATH,"//label[text()='Monday']/preceding-sibling::input[@id='monday']")
# radio_button.click()
# print(radio_button.text)
# sleep(4)

# n=input('write m for male and f for female')
# if n == 'm':
#     radio_button = driver.find_element(By.XPATH, "//input[@id='male']")
#     radio_button.click()
# else:
#     radio_button = driver.find_element(By.XPATH, "//input[@id='female']")
#     radio_button.click()


# def rec(length,i):
#     if(length<=0):
#         return
#     driver.find_element(By.XPATH, f"//label[@for='days']/following-sibling::div[{i}]/input").click()
#     print(driver.find_element(By.XPATH,f"//label[@for='days']/following-sibling::div[{i}]/label").text)
#     rec(length-1,i+1)
#     driver.find_element(By.XPATH, f"//label[@for='days']/following-sibling::div[{i}]/input").click()
# def funcn():
#     driver.get('https://testautomationpractice.blogspot.com/')
#     length=len(driver.find_elements(By.XPATH,"//label[@for='days']/following-sibling::div/input"))
#     rec(length,1)
# funcn()


# driver.get("https://www.flipkart.com")
# sleep(2)
# button_cross=driver.find_element(By.XPATH,"//span[text()='✕']")
# button_cross.click()
# sleep(2)
# search_field=driver.find_element(By.XPATH,"//input[@class='nw1UBF v1zwn25']")
# search_field.clear()
# search_field.send_keys("Asus Rog")
# sleep(2)
# print(search_field.get_attribute("value"))   # value will return us the value only
# search_button=driver.find_element(By.XPATH,"//button[@type='submit']")
# search_button.click()
# sleep(2)
# filter_cl=driver.find_element(By.XPATH,"//div[@title='4★ & above']/descendant::div[@class='ybaCDx']")
# filter_cl.click()
# print(filter_cl.text)
# sleep(2)




'''
var_name.is_displayed()  -> gives true if it is visible on screen
var_name.is_enabled()    -> gives true if a button is enabled or not (only for buttons)  use only after writing in a text field
var_name.is_selected()   -> gives true if a checkbox,radio is selected or not
'''

# driver.get('https://testautomationpractice.blogspot.com/')
# sleep(5)
# female=driver.find_element(By.ID,'female')
# print(female.is_displayed())
#
# sunday_button=driver.find_element(By.ID,'sunday')
# sunday_button.click()
#
# print(sunday_button.is_enabled())
#
# print(sunday_button.is_selected())
#
# name_button=driver.find_element(By.ID,'name')
# # name_button.send_keys('hello')
#
# print(name_button.is_enabled())           # True bcoz we can write in it

# print(name_button.is_selected())


'''
assert :- 
is assert true if an element is there and will continue to execute next line 
or 
return assertion error otherwise'''


driver.get('https://www.lenskart.com/')
sleep(3)

eye_glass=driver.find_element(By.ID,'lrd1')

assert 'EYEGLASSES' in eye_glass.text,'couldnt find'         # if cant find will return couldnt find

driver.quit()