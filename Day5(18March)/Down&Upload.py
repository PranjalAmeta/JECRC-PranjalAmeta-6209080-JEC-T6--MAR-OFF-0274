from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
sleep(2)
choose=driver.find_element(By.ID,"file-upload")
choose.send_keys("C://Users//Pranjal Ameta//OneDrive//Desktop//Selenium&Robot//Projects//Day4(16March)//Problem_Statement.md")

button_up=driver.find_element(By.ID,"file-submit")
button_up.click()
sleep(5)


driver.get('https://the-internet.herokuapp.com/download')
driver.maximize_window()
driver.find_element(By.XPATH,'//a[text()="Screenshot 2025-12-24 164603.png"]').click()
sleep(10)
print('downloaded')