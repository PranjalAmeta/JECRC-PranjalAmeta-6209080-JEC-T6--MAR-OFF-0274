*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  3s
    Click Element  xpath=//button[@onclick='jsAlert()']
    Sleep  2s
    Handle Alert
    Sleep  2s
    Close Browser

Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  3s
    Click Element  xpath=//button[@onclick='jsConfirm()']
    Sleep  2s
    Handle Alert  action=CONFIRM
    Sleep  2s
    Close Browser


Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  3s
    Click Element  xpath=//button[@onclick='jsPrompt()']
    Sleep  2s
    Input Text Into Alert  hello  # action=DISMISS -> if you want to dismiss
    Sleep  2s
    Close Browser