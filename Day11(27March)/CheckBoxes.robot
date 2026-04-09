*** Settings ***
Documentation  Handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling Checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  3s
    Click Element  xpath=//a[text()='Checkboxes']
    # similar to assert we can use pages should contain attribute_val
    Page Should Contain Checkbox  xpath=//input[@type='checkbox'][1]
    Select Checkbox  xpath=//input[@type='checkbox'][1]
    Sleep  2s
    Unselect Checkbox  xpath=//input[@type='checkbox'][1]
    sleep  2s

Handling on Test automation prac Site
    Open Browser  https://testautomationpractice.blogspot.com/  chrome
    Maximize Browser Window
    Sleep  3s
    Select Checkbox   //input[@id='monday']
    sleep  2s
    Unselect Checkbox    //input[@id='monday']
    Sleep  2s