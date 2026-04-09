*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling Iframes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Select Frame  id=singleframe
    Input Text  //input[@type='text']  ky Bolti public
    Sleep  5s
    Close Browser


Handling Nested Frame
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element  //a[@href='#Multiple']
    Sleep  2s
    Select Frame  xpath=//iframe[@src='MultipleFrames.html']
    Select Frame  xpath=//iframe[@src='SingleFrame.html']
    Input Text  //input[@type='text']  ky Bolti public
    Sleep  5s
    UnSelect Frame         # returns to default content/Frame
    Close Browser