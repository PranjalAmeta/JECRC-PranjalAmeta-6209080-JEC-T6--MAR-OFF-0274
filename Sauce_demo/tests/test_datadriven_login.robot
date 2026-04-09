# Doing this in a single file only
*** Settings ***
Resource  ../resource/common_resources.robot
# data driver is a module which will read our excel sheet where each row behave as a testcase
Library  DataDriver  ../test_data/Data Driven.xlsx  sheet_name=Sheet1


# data driven testing:-

# Data driver creates test
# test template defines what test case does
# Test Template :- for going to a test case in data driven testing we need loops same way we have this under test
# template  and the function keyword
# test template  funcn_name

# the [arguments]  ${user_creds}  ${pass_creds} should be inside data driven file only

# https://chatgpt.com/share/69d0a7f9-1c44-8322-b181-720b78d40a83


Test Setup    Open Application  https://www.saucedemo.com/
Test Teardown  Close Application
Test Template  Login to application using excel

*** Variables ***
${USERNAME}  id=user-name
${PASSWORD}  id=password
${LOGINBUTTON}  id=login-button


*** Test Cases ***
Execl Data Driven Testing  ${user_creds}  ${pass_creds}
    [Documentation]  This test case is to perform data driven testing from excel
    [Tags]  Data Driven
    
*** Keywords ***
Login to application using excel
    [Arguments]  ${user_creds}  ${pass_creds}
    Input Text  ${USERNAME}  ${user_creds}
    Input Text  ${PASSWORD}  ${pass_creds}
    Click Button  ${LOGINBUTTON}
    
    
# Parallel Exectution of tests 
# pabot --processes 4 --testlevelsplit -d reports tests







