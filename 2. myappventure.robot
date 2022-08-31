*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}    http://myappventure.herokuapp.com/registration
${name}    aaaa
${email}    a@gmail.com
${pass}    1234


*** Keywords ***
Open page
    Open browser    ${url}    chrome

Register
    Input Text    name=username    ${name}
    Input Text    name=email    ${email}
    Input text    name=password    ${pass}
    Click element    xpath=//*[@id="__next"]/main/div/div/form/div[5]/button
    Close Browser
   
Sign in
    Click Element    xpath=//*[@id="__next"]/main/div/div/form/div[5]/div/p/a
    Input Text    name=email   ${email}
    Input text    name=password    ${pass}
    Click element    xpath=//*[@id="__next"]/main/div/div/form/div[4]/button
    Close browser
    
*** Test Cases ***
Sign Up myappventure
    Open page
    Register

Sign in myappventure
    Open page
    Sign in
