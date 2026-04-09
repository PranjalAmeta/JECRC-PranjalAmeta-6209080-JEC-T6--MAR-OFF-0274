'''
Action chains is a class that contains mouse or keyboard methods
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


# driver=webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(2)
# action=ActionChains(driver)
#
# org_el=driver.find_element(By.ID,'column-a')
# tar_el=driver.find_element(By.ID,'column-b')
#
# action.drag_and_drop(org_el,tar_el).perform()
# sleep(2)

# driver=webdriver.Chrome()
# driver.get('https://www.supertails.com')
# actions=ActionChains(driver)
# driver.maximize_window()
# sleep(2)
# element=driver.find_element(By.XPATH,"(//span[contains(text(),'Dogs')])[1]")
# actions.move_to_element(element).perform()
# sleep(3)

'''
driver=webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(2)
action=ActionChains(driver)
org_element=driver.find_element(By.XPATH,"(//div[@id='draggable'])[1]")
tar_el=driver.find_element(By.XPATH,"(//div[@id='droppable'])[1]")
action.drag_and_drop(org_element,tar_el).perform()
sleep(5)
assert "Dropped!"==tar_el.text,"not found"
'''

# driver=webdriver.Chrome()
# driver.get('https://demoqa.com/droppable')
# driver.maximize_window()
# sleep(2)
# wait=WebDriverWait(driver,10)
# action=ActionChains(driver)
# prevent_tab_key=wait.until(element_to_be_clickable((By.ID,'droppableExample-tab-preventPropogation')))
# prevent_tab_key.click()
# org_el=driver.find_element(By.XPATH,"//div[@id='dragBox']")
# tar_el=driver.find_element(By.ID,"greedyDropBoxInner")
# action.drag_and_drop(org_el,tar_el).perform()
# sleep(2)

''' ------ Scroll to Element ----- '''

# driver=webdriver.Chrome()
# driver.get('https://supertails.com/')
# driver.maximize_window()
# wait=WebDriverWait(driver,10)
# action=ActionChains(driver)
# rabitto=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@data-ganame='Breed 5']")))
# action.scroll_to_element(rabitto).perform()
# sleep(6)


'''
scroll_to :- will go to a exact point like (x,y)                                 (cant give negative values)
scroll_by :- will go to req position from the current psition so it is relative   (can give negative values)
scroll_by_amount(x,y).perform():- in the form of axes  
scroll_from_origin(origin,x,y)
'''


''' ------ Keyboard Actions ------ '''
'''
action=ActionChains(driver)

action.send_keys(Keys.PAGE_DOWN)  # 100px down
action.send_keys(Keys.PAGE_UP)    # 100px up
action.send_keys(Keys.END)
action.send_keys(Keys.HOME)
Keys.DOWN :- similar to pressing down a button
Keys.UP :- Similar to depressing the button

CONTROL is used as ctrl+a,c,v
'''
# driver=webdriver.Chrome()
# driver.get('https://supertails.com/')
# action=ActionChains(driver)
# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(2)
# action.send_keys(Keys.PAGE_UP).perform()
# sleep(2)
# action.send_keys(Keys.END).perform()                     # End of the page
# sleep(2)
# action.send_keys(Keys.HOME).perform()                    # Home page
# sleep(2)

# driver.maximize_window()
# driver.get("https://amazon.com")
# action.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(2)
# action.key_up(Keys.CONTROL).perform()   # release the ctrl key
# sleep(2)
# action.key_down(Keys.CONTROL).send_keys('c').perform()
# sleep(2)
# action.key_up(Keys.CONTROL).perform()
# wait=WebDriverWait(driver,10)
# el=wait.until(EC.element_to_be_clickable((By.ID,"twotabsearchtextbox")))
# el.click()
# # el.send_keys("asbc",Keys.ENTER)
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(2)



# Password Visibility

driver=webdriver.Chrome()
driver.get(r"C:\Users\Pranjal Ameta\OneDrive\Desktop\Selenium&Robot\Projects\Day8(23march)\Password.html")
driver.maximize_window()
action=ActionChains(driver)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("********")
sleep(2)
eyebtn=driver.find_element(By.XPATH,"//button[@id='eyeBtn']")
action.click_and_hold(eyebtn).perform()
action.release(eyebtn).perform()
sleep(2)


