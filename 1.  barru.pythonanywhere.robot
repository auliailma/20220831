*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}    http://barru.pythonanywhere.com/daftar
${name}    aaaa
${email}    a@gmail.com
${pass}    1234


*** Keywords ***
Open page
    Open browser    ${url}    chrome

Sign up
    Click Element    id=signUp

Register
    Input Text    id=name_register    ${name}
    Input Text    id=email_register    ${email}
    Input Text    id=password_register    ${pass}
    Click element    id=signup_register
    Close Browser
   
Sign in
    Input Text    id=email   ${email}
    Input text    id=password    ${pass}
    Click element    id=signin_login
    Close browser
    
*** Test Cases ***
Sign Up
    Open page
    Sign up
    Register

Sign in
    Open page
    Sign in
