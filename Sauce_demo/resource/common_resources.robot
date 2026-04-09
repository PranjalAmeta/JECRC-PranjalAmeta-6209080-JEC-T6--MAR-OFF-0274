# Anything under .py files will come under Library
# Anythng under robot will come under Resource
*** Settings ***
Library  SeleniumLibrary
Library  ../config/env_loader.py

*** Variables ***
${BROWSER}  chrome
${ENV}  qa

*** Keywords ***
#Load Environment
#    Load Env    ${ENV}
#    ${BASE_URL}=  Get Env  BASEURL
#    ${FIRST_NAME}=  Get Env  FIRST_NAME
#    ${LAST_NAME}=  Get Env  LAST_NAME
#    ${EMAIL}=  Get Env  EMAIL
#    ${PASSWORD}=  Get Env  PASSWORD
#
#
#
#
#    SET GLOBAL VARIABLE   ${BASE_URL}
#    SET GLOBAL VARIABLE   ${FIRST_NAME}
#    SET GLOBAL VARIABLE   ${LAST_NAME}
#    SET GLOBAL VARIABLE   ${EMAIL}
#    SET GLOBAL VARIABLE   ${PASSWORD}

Open Application 
    [Documentation]  Opens the application
    [Arguments]  ${URL}
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window

Close Application
    Close All Browsers
    