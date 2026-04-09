# Only the user interaction
*** Settings ***
Library  SeleniumLibrary
Resource    ../../locators/sign_up.robot

*** Keywords ***
Sign Up To The Application
    [Documentation]  this registers the users
    [Arguments]  ${first_name}  ${last_name}  ${email}  ${pwd}
    
    Click Element  ${signup_link}
    Log  Clicking on sign up link

    # Input Text  locator  text_value
    Input Text  ${first_name_field}  ${first_name}
    Log  Entering First Name 
    
    Input Text  ${last_name_field}  ${last_name}
    Log  Entering Last Name 
    
    Input Text  ${email_field}  ${email}
    Log  Entering Email 
    
    Input Text  ${pwd_field}  ${pwd}
    Log  Entering Password
    
    Click Element  ${create_button}
    Log  Clicking on create