*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/Log_in_locator.robot

*** Keywords ***
Log In To Application
    [Documentation]  is the user able to login
    [Arguments]    ${email}  ${pwd}
    
    Click Element  ${log_in_btn}
    Log  Clicking the login Button
    
    Input Text  ${email_field}  ${email}
    Log  Entering email
    
    Input Text  ${pwd_field}  ${pwd}
    Log  Entering Password

    Click Element  ${sign_in_btn}
    Log  Clicking the button