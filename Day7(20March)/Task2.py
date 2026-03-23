from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()
driver.get(r"C:\Users\Pranjal Ameta\OneDrive\Desktop\Selenium&Robot\Projects\Day7(20March)\playlist.html")

drop_sel=driver.find_element(By.ID,'songs')

select=Select(drop_sel)

fav_artist='Tame Impala'#input('enter favourite artist:')

options_el=driver.find_elements(By.XPATH,f"//select[@id='songs']/optgroup[@label='{fav_artist}']/option")
#print(len(options_el))
# l=options_el.text.split("\n")

for opt in options_el:
     select.select_by_visible_text(opt.text)
sleep(4)
