*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://practicetestautomation.com/practice-test-login/

*** Test Cases ***
Implicit wait          # that applies to all the elements
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait      # Returns the time of implicit wait
    Log To Console  ${before}
    Set Selenium Implicit Wait    5s           # Set The time of implicit wait
    ${after}  Get Selenium Implicit Wait       
    Log To Console  ${after}
    Close Browser
# Set Browser Implicit Wait -> set implicit wait for one browser instance 
# If there are Multiple Browser then it will be confined to that browser   

Explicit Wait           # That applies to individual element
    Open Browser  ${url1}  chrome

    Wait Until Element Is Visible  id=username
    Input Text  id=username  student

    Wait Until Element Is Visible  password
    Input Text  password  Password123

    Wait until Element Is Enabled  submit
    Click Element  id=submit

    Wait Until Location Contains  logged-in-successfully

    Close Browser

    
    
    