*** Settings ***
Library  SeleniumLibrary
Resource  resource/common_resources.robot

# cross browser
*** Test Cases ***
tc1
    Open Application    https://sauce-demo.myshopify.com
    Sleep  2s
    Close Application