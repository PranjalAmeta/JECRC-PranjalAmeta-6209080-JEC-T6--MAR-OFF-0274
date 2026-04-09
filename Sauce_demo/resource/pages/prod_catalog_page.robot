*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/Prod_catalog_locator.robot

*** Keywords ***
Search For a Product
    [Documentation]  Searching for a product
    [Arguments]  ${Input_Text}
    
    Sleep  10s
    
    Click Element  ${prod_click}
    Log  Clicking in to search field
        
    Input Text  ${search_inp}  ${Input_Text}
    Log  Entering the input text
        
    Click Element  ${search_sbmt}
    Log  Clicking the search button