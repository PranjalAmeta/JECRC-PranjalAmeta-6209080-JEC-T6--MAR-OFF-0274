*** Settings ***
Resource  ../../resource/pages/sign_up_page.robot
Resource  ../../resource/common_resources.robot

# Setup and teardown :- used in settings
# 1) suite setup and teardown :- common for whole session,opens browser runs all test files and then closes
#      :- if a test case is failed it will stop working as it is not confined in one test case only
# 2) test setup and teardown :- similar to explicit wait :- applies to individual test ,open browser for each test case

# data driven testing:- 

# Test Template :- for going to a test case in data driven testing we need loops same way we have this under test
# template  and the function keyword
# test template  funcn_name

# the [arguments]  ${user_creds}  ${pass_creds} should be inside data driven file only
Suite Setup  Load Environment
Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***
TC01 Register User
    [Documentation]  check if the user is able to register
    [Tags]  functional

    Sign Up To The Application  ${FIRST_NAME}  ${LAST_NAME}  ${EMAIL}  ${PASSWORD}