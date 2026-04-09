*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login
    Open Browser  ${url}  chrome
    Maximize Browser Window
    # Positional Args
#    Login Success  abc@gmail.com  iamironman
#    Sleep  2s
    # default
#    Login Success  abc@gmail.com
#    Sleep  2s
#    Login Success  abc@gmail.com  Prank
#    Sleep  2s
#    #keyword
    Login Success  pwd=abc@gmail.com  email=iamironman
    Sleep  2s


# Keywords acts as an functions or methods
*** Keywords ***
# Write only one argument at a time
Login Success
    # Normal 
    # Input Text id=customer_email  abc@gmail.com
    # Positional arguments
#    [Arguments]  ${email}  ${pwd}
    # Default arguments
#    [Arguments]  ${email}  ${pwd}=iamironman
#    # Keyword Arguments :-given during function calling
    [Arguments]  ${email}  ${pwd}
    Input Text  id=customer_email  ${email}
    Input text  id=customer_password  ${pwd}
    
    
    
    
 