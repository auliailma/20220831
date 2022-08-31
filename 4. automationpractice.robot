*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}    http://automationpractice.com/index.php
${name}    aaaa
${email}    a@gmail.com
${pass}    1234
${search}    summer


*** Keywords ***
Open page
    Open browser    ${url}    chrome

Login
    Click Element    xpath=//*[@id="header"]/div[2]/div/div/nav/div[1]/a

Register
    Input Text    id=email_create    ${email}
    Click element    xpath=//*[@id="SubmitCreate"]
    Close Browser
   
Sign in
    Input Text    id=email   ${email}
    Input text    id=passwd    ${pass}
    Click element    id=SubmitLogin
    Close browser

Search
    Input Text    id=search_query_top    ${search}
    Click Element    name=submit_search
    Close Browser
    
*** Test Cases ***
Sign Up
    Open page
    Login
    Register

Signin
    Open page
    Login
    Sign in

Search products
    Open page
    Search
