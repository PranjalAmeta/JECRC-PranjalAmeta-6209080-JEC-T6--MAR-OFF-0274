# Example  of multi select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome()

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# mutli_sel=driver.find_element(By.ID,"colors")
#
# select=Select(mutli_sel)
#
# if select.is_multiple():
#     print(select.select_by_value('green'))
#     print(select.select_by_text_value('red'))




# NOTE :- print(select.options()) :- returns all the options
# All the methods are applied on options only after select
#################################################

driver.get(r"C:\Users\Pranjal Ameta\OneDrive\Desktop\Selenium&Robot\Projects\Day7(20March)\playlist.html")

drop_sel=driver.find_element(By.ID,'songs')

select=Select(drop_sel)

if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text("Photography")


driver.find_element(By.XPATH,"//button[text()='Add to Playlist']").click()

print([i.text for i in select.options])

print([i.text for i in select.all_selected_options])

sleep(4)