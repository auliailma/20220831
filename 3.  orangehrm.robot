*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/
${username}    Admin
${password}    admin123
${firstname}    Lize
${middlename}    Helesta
${lastname}    Katrina


*** Keywords ***
Open page
    Open browser    ${url}    chrome
    Wait Until Page Contains Element    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input

Login
    Input text   name=username    ${username}
    Input text    name=password    ${password}
    Click element    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    Wait Until Page Contains Element    xpath=//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button
    # Close browser

Add employee
    Click Element    xpath=//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button
    Wait Until Page Contains Element    xpath=//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]
    Input Text    name=firstName    ${firstname}
    Input Text    name=middleName    ${middlename}
    Input Text    name=lastName    ${lastname}
    Click button   xpath=//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]
    Close Browser

*** Test Cases ***
Login orangehrmlive
    Open page
    Login

Add new employee
    Add employee
