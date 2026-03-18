from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')
sleep(5)

first_name=driver.find_element(By.ID,'firstName')
first_name.clear()
first_name.send_keys('Pranjal')


last_name=driver.find_element(By.ID,'lastName')
last_name.clear()
last_name.send_keys('Ameta')


email=driver.find_element(By.ID,'userEmail')
email.clear()
email.send_keys('prank@gmail.com')

gender=driver.find_element(By.ID,'gender-radio-1')
gender.click()

mobile_num=driver.find_element(By.ID,'userNumber')
mobile_num.clear()
mobile_num.send_keys('0987654321')

subject=driver.find_element(By.ID,'subjectsInput')
subject.clear()
subject.send_keys('PCM')


hobbies_one=driver.find_element(By.ID,'hobbies-checkbox-1')
hobbies_one.click()

hobbies_two=driver.find_element(By.ID,'hobbies-checkbox-3')
hobbies_two.click()

pic=driver.find_element(By.ID,'uploadPicture')
pic.send_keys(r"C:\Users\Pranjal Ameta\OneDrive\Pictures\pedro.jpeg")

address=driver.find_element(By.ID,'currentAddress')
address.clear()
address.send_keys('dhabe pe')

state=driver.find_element(By.ID,'react-select-3-input')
state.send_keys('Rajasthan',Keys.ENTER)

city=driver.find_element(By.ID,'react-select-4-input')
city.send_keys('Jaipur',Keys.ENTER)

sleep(3)
submit_button=driver.find_element(By.ID,'submit')
submit_button.click()

sleep(3)
driver.quit()