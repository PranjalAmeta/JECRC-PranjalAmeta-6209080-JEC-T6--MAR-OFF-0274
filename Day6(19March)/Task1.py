from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get('https://www.abc.com')
wait=WebDriverWait(driver,10)

imgs=wait.until(EC.presence_of_all_elements_located((By.XPATH,r"//div[@class='tile--hero__container']/descendant::picture/img")))

for img in imgs:
    print(img.get_attribute('src'))

