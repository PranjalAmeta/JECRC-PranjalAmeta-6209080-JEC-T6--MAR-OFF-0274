from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
driver.get("https://qavbox.github.io/demo/signup/")

wait=WebDriverWait(driver,6)

name=wait.until(EC.presence_of_element_located((By.ID,"username")))
name.clear()
name.send_keys("Pranjal Ameta")

email=wait.until(EC.presence_of_element_located((By.ID,"email")))
email.clear()
email.send_keys("pranjal@mail.com")

num=wait.until(EC.presence_of_element_located((By.ID,"tel")))
num.clear()
num.send_keys("0987654321")

# fax_num=wait.until(EC.presence_of_element_located((By.ID,"fax")))
# fax_num.clear()
# fax_num.send_keys("29122")

file=wait.until(EC.element_to_be_clickable((By.NAME,"datafile")))
if(file.is_enabled()):
    file.send_keys(r"C:\Users\Pranjal Ameta\OneDrive\Pictures\pedro.jpeg")

gender_el=wait.until(EC.presence_of_element_located((By.NAME,"sgender")))
select=Select(gender_el)
select.select_by_value("male")

exp_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='one']")))
if(exp_button.is_enabled()):
    exp_button.click()

skills=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='automationtesting']")))
if(skills.is_enabled()):
    skills.click()

tool_el=wait.until(EC.presence_of_element_located((By.ID,"tools")))
select=Select(tool_el)
select.select_by_value("selenium")

submit=wait.until(EC.element_to_be_clickable((By.ID,"submit")))
if(submit.is_enabled()):
    submit.click()
sleep(2)
driver.quit()

