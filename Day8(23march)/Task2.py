from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.myntra.com")
driver.maximize_window()
wait=WebDriverWait(driver,10)

men_button=wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Men']")))

action=ActionChains(driver)
action.move_to_element(men_button).perform()

button_sel=wait.until(EC.presence_of_element_located((By.XPATH,"//li[@data-reactid='38']")))
button_sel.click()

scroll_el=wait.until(EC.presence_of_element_located((By.XPATH,"//li[@id='37075364']")))
action.scroll_to_element(scroll_el).perform()
sleep(3)

