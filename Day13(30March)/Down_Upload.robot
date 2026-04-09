*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_down}  C:\\Users\\Pranjal Ameta\\Downloads\\file.txt
*** Test Cases ***
Upload
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element  //a[@href="/upload"]
    # Choose File  id=file-upload  "C://..path"  # Wont work
    ${path}  Normalize Path  C:\\Users\\Pranjal Ameta\\OneDrive\\Pictures\\pedro.jpeg  #${CURDIR}/wait.robot
    Choose File  id=file-upload  ${path}
    Click Element  id=file-submit

    Close Browser
    
Download
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element  //a[@href="/download"]
    Sleep  2s
    Click Element  //a[@href="download/file.txt"]
    Sleep  2s
    Wait Until Created    ${check_down}  timeout=10s
    File Should Exist    ${check_down}
    Log to Console  File downloaded Successfully
    Close Browser