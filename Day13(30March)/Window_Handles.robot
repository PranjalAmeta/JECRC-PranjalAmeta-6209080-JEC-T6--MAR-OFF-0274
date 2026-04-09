*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
Handling windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s
    Click Element  //a[@href='/windows/new']
    Sleep  2s
    @{windows}  Get Window Handles    
    @{titles}  Get Window Titles    
    Log To Console  ${titles}
    Switch Window  NEW   # Will switch to new window
    Page Should Contain    New Window
              # OR
    # Page Should Contain  xpath=//h3[text()='New Window']
    Switch Window  ${windows}[0]
    
    Sleep  2s
    
    Close Window
    Sleep  2s
    Close Browser