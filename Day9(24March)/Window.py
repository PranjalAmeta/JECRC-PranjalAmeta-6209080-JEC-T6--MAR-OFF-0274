from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(2)
parent_window=driver.current_window_handle
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()

all_windows=driver.window_handles
print(len(all_windows))

driver.switch_to.window(all_windows[-1])
sleep(2)
assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
print('done')
driver.close()
# if i use driver.close() it will close the window but the control will be in that window only
driver.switch_to.window(parent_window)
sleep(2)


# Opening a website in a new window
driver.get('https://the-internet.herokuapp.com/windows')
driver.switch_to.new_window('window')    # will create a new window
# driver.switch_to.new_window('tab')       # new tab
driver.get('https://the-internet.herokuapp.com/windows')
sleep(2)

