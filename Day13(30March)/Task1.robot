*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Window
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s
    Log Title
    Click Element  xpath=//button[@id='PopUp']
    Sleep  2s
    Switch Window  NEW
    @{windows}  Get Window Handles
    @{new_title}  Get Window Titles    
    Log To Console  ${new_title}
    Switch Window  ${windows}[0]
    Page Should Contain  Automation Testing Practice
    Sleep  2s
    Close Browser