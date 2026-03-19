# To deal with synchronization issues we use wait
# issues such as ram, latency ,speed,dom loading and so on
'''
Using time.sleep() in Selenium is not recommended because it blindly waits
for a fixed time, even if the element is ready earlier

# To overcome this we use waits :-
-> Implicit waits:- Waits globally for elements to appear.
                    for every element it will wait upto specified sec.
                    Not flexible (applies to all elements[driver.find_element])
                    will not care if the element is visible or not
                    Worst case:
                    1st element → 10 sec
                    2nd element → 10 sec
                    3rd element → 10 sec
                    If element found early then - selenium stops waiting
                    -> will give no element found exception.
                    driver.implicitly_wait(sec)
-> Explicit waits:- Waits for a specific condition.   ( Use this only )
                    Confined to a particular element.
                    -> will give time out error
                    # Syntax:-
                    WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
                    -> timeout for how much time it will wait (in sec)
                    -> how often selenium checks the condn (by default it is 0.5 sec)
                    ->
-> fluent wait -> More control (polling + ignore exceptions)
'''
from astropy.io.misc.yaml import tag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait  # Used for explicit wait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
# driver.get('https://www.amazon.com')
# driver.implicitly_wait(5)
#
# driver.find_element(By.ID,'glow-ingress-line1')
# print('el found')


# wait_obj=WebDriverWait(driver,10,0.2)

# search_field=wait_obj.until(EC.element_to_be_clickable((By.ID,'twotabsearchtextbox')))
# search_field.click()
# driver.quit()


# driver.get('https://www.abc.com')
# wait_obj2=WebDriverWait(driver,10)
# loading_symbol=wait_obj2.until(EC.invisibility_of_element_located((By.ID,'preloader-animated_svg__svg3')))
#
# title_abc=wait_obj2.until(EC.presence_of_element_located((By.XPATH,"//span[text()='ABC SHOWS, SPECIALS & MORE']")))
#
# assert 'SPECIALS' in title_abc.text,'ABC SHOWS, SPECIALS & MORE'
#
# print('working fine')
# driver.quit()


driver.get('https://demoqa.com/dynamic-properties')
wait_obj3=WebDriverWait(driver,6)

enabled_before=driver.find_element(By.ID,'enableAfter')
print('is it clickable before: ',enabled_before.is_enabled())

enabled_after=wait_obj3.until(EC.element_to_be_clickable((By.ID,'enableAfter')))

if(enabled_after.is_enabled()):
    enabled_after.click()
    print('button is clickable now')

visible_el=wait_obj3.until(EC.element_to_be_clickable((By.ID,'visibleAfter')))
visible_el.click()


# Select Methods:-
## select.is_multiple() --> if the options are multiple select or single select (True/False)
## select.deselect_by_index(index),by_visible_text(),by_value()
## select.deselect_all() --> deselects all option
## first_selected_option --> not a method/function; returns the first selected option; returns none
## all_selected_options --> not a method/function; returns list of options selected