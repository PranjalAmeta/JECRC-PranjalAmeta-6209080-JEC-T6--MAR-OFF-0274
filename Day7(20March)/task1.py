from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()
driver.get(r"C:\Users\Pranjal Ameta\OneDrive\Desktop\Selenium&Robot\Projects\Day7(20March)\playlist.html")

drop_sel=driver.find_element(By.ID,'songs')

select=Select(drop_sel)

l=[i.text for i in select.options]
for i in l:
    if('girl' in i.lower() or 'love' in i.lower()):
        select.select_by_visible_text(i)

print([i.text for i in select.all_selected_options])

sleep(5)