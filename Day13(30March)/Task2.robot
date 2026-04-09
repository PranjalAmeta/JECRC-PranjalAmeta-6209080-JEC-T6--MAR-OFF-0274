*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element  id=alertBtn
    Handle Alert
    Close Browser

Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element  id=confirmBtn
    Handle Alert  action=DISMISS
    Sleep  2s
    ${output}  Get Text  //p[@id='demo']
    Page Should Contain  You pressed Cancel
    Log To Console  ${output}
    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element  id=promptBtn
    Input Text Into Alert   Level
    Sleep  2s
    ${output}  Get Text  //p[@id='demo']
    Page Should Contain  Hello Level! How are you today?
    Log To Console  ${output}
    Close Browser