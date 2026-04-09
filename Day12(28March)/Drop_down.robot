
# for choosing option manually create the variable and use:- robot -v OPTION:'val'  name.robot

*** Settings ***
Documentation  Handling dropdowns
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/
${optionchoosen}  Option 1               # can also choose browser :- cross browser testing
*** Test Cases ***
handle dropdown
    [Documentation]  navigated to herokuapp
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element  //a[text()='Dropdown']
    # 1st assert
    Page Should Contain List  id=dropdown   # similar to page should contain element but list is preffered
    
    ${options}=  Get List Items    id=dropdown
    Log To Console  ${options}
    Select From List By Label    id=dropdown  ${optionchoosen}   # takes 2 args  locater and label,index,value
    
    ${select_option}=  Get Selected List Label    id=dropdown
    Log To Console  ${select_option}
    
    List Selection Should Be  id=dropdown  ${select_option}

    sleep  3s
    Close Browser
    
Handling testautomationpractice
    [Documentation]  Handling colors
    Open Browser  ${url1}  chrome
    Maximize Browser Window
    Page Should Contain List  //select[@id='colors']
    Scroll Element Into View  //select[@id='colors']
    ${option}=  Get List Items   //select[@id='colors']
    Log To Console  ${option}
    Select From List By Label   //select[@id='colors']  Red  Blue  Yellow
    @{selected_opt}=  Get Selected List Label  //select[@id='colors']
    # will return list if $ is used it will become nested list [[opt1,opt2]]
    Log To Console  ${selected_opt}
    List Selection Should Be  //select[@id='colors']  @{selected_opt}
    Sleep  3s
    Close Browser