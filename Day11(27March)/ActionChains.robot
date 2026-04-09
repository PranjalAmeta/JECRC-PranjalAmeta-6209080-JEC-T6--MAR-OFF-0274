*** Settings ***
Documentation  Handling action chains
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
#Handling Drag and drop
#    [Documentation]  navigating to herokuapp
#    Open Browser  ${url}  chrome
#    Click Element    //a[text()='Drag and Drop']
#    sleep  2s
#    Drag and Drop  id=column-a  id=column-b          # Drag and Drop  src  dest
#    sleep  2s
#    Close Browser
#
    
Handling Mouse Hover
    Open Browser  ${url}  chrome
    sleep  1s
    Click Element   //a[text()='Hovers']
    sleep  2s
    Mouse Over  //div[@class='figure'][2]
    sleep  2s
    Close Browser

Scroll To The Element
    Open Browser  ${url}  chrome
    sleep  1s
    Scroll Element Into View    //a[text()='Typos']
    sleep  10s
    Close Browser