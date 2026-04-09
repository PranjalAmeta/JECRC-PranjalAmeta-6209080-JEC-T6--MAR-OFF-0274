*** Settings ***
Resource  ../../resource/pages/prod_catalog_page.robot
Resource  ../../resource/common_resources.robot

Suite Setup    Load Environment
Test Setup    Open Application
Test Teardown  Close Application

*** Test Cases ***
TC01 Searching Product
    [Documentation]  searching for product
    [Tags]  functional
    Search For a Product  jacket