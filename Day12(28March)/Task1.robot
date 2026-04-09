*** Settings ***
Documentation  Handling Multiselect
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Multiselection
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Page Should Contain List    id=colors
    ${options}=  Get List Items    id=colors
    Log To Console    ${options}


    Select From List By Label    id=colors  Blue
    Sleep    1s

    Select From List By Label    id=colors  Yellow
    Sleep    1s

    @{selected_options}=  Get Selected List Labels    id=colors
    Log To Console    ${selected_options}

    List Selection Should Be    id=colors  @{selected_options}
    Sleep    3s

    Close Browser