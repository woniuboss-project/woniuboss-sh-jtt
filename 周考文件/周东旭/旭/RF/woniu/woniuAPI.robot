*** Settings ***
Library           RequestsLibrary

*** Variables ***
&{headers}        Content-Type=application/x-www-form-urlencoded

*** Test Cases ***
login

*** Keywords ***
login
    [Arguments]    ${phone}    ${password}
    ${body}    Create Dictionary    phone    ${phone}    password=123456    ${password}
    Create Session    session    https://snailpet.com/index
    ${resp}    Post Request    session    /welcome    ${body}    headers=${headers}
    Run Keyword If    ${resp.json()['error']}==1    Log    login_pass
    ...    ELSE    Log    login_fail
