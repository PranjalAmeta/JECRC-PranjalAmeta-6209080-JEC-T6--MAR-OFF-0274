*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/ScreenShots  #${CURDIR} will give us the current dir
    # if i write ${CURDIR}/../Screenshots :- it will go to the ScreenShot in projects folder not in this one
    [Tags]  smoke
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s
    Capture Page Screenshot    fullPage.png
    Sleep  2s
    Capture Element Screenshot    //span[text()='Our Achievements']  achieve.png
    Sleep  2s

    Close Browser
