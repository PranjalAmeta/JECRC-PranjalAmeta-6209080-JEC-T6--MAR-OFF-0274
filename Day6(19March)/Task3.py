from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.amazon.com")
driver.maximize_window()
wait=WebDriverWait(driver,10)
search_box=wait.until(EC.element_to_be_clickable((By.ID,"twotabsearchtextbox")))
search_box.send_keys("asus rog")

recommend=wait.until(EC.presence_of_element_located((By.ID,'sac-suggestion-row-4')))
if recommend.is_displayed():
    recommend.click()

sort_but=wait.until(EC.element_to_be_clickable((By.ID,'a-autoid-0-announce')))
sort_but.click()

new_arrival=wait.until(EC.element_to_be_clickable((By.ID,'s-result-sort-select_4')))
new_arrival.click()

# free_ship=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@id='p_n_free_shipping_eligible/205563695031']/descendant::input")))
# free_ship.click()

name=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@role='listitem']/descendant::h2/descendant::span")))
print(name.text)

price=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@role='listitem'][1]/descendant::span[@class='a-offscreen'][1]")))
print(price.get_attribute("textContent"))


driver.quit()