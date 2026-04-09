*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Handling Amazon
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Wait Until Location Contains   www.amazon.in
    Wait Until Element Is Enabled  //a[text()=' Electronics ']
    Click Element  xpath=//a[text()=' Electronics ']
    Click Element  //label[@for='apb-browse-refinements-checkbox_6']/descendant::i
    ${name}  Get Text  //span[contains(text(),'Boat Rockerz')]
    Click element  //span[contains(text(),'Boat Rockerz')]
    Switch Window  New
    # Log To Console  ${name}
    Wait Until Page Contains  ${name}  5s
    ${discount}  Get Text  //span[@class="apex-savings-container"]/span
    ${dis_prize}  Get Text  //span[@class="apex-savings-container"]/following-sibling::span/descendant::span[4]
    ${act_prize}  Get Text  (//span[@class="a-price a-text-price apex-basisprice-value"]/span)[1]
    Log To Console  ${discount}
    Log To Console  ${dis_prize}
    Log To Console  ${act_prize}
    Scroll Element Into View    add-to-cart-button
    Click Element  add-to-cart-button
    Click Element  nav-cart-count-container
    Wait Until Page Contains  ${name}  5s