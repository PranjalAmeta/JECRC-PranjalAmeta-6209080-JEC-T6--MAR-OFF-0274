*** Settings ***
Resource  ../../resource/common_resources.robot
Resource  ../../resource/pages/Log_in_page.robot

Test Setup    Open Application  https://sauce-demo.myshopify.com/account/login
Test Teardown    Close Application

*** Test Cases ***
Checking Login
    [Documentation]  Check if the user is able to login
    [Tags]  functional
    
    Log In To Application  abc@gmail.com  abc
