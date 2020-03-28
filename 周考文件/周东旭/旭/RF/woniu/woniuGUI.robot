*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
login
    [Setup]
    [Template]    login
    17766086297    123456

customer
    [Template]    customer
    周周    17766086297    小猫

*** Keywords ***
login
    [Arguments]    ${phone}    ${pass}
    Open Browser    https://snailpet.com/index
    Sleep    5
    Click Element    class:red_btn
    sleep    3
    Input Text    name:phone    ${phone}
    Input Password    name:password    ${pass}
    Click Element    xpath:/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Wait Until Page Contains Element    link=安全退出
    ${quit}    Get Text    link=安全退出
    Should Contain    ${quit}    安全退出
    Close Browser

customer
    [Arguments]    ${name}    ${phone}    ${animal}
    Open Browser    https://snailpet.com/index
    Sleep    5
    Click Element    class:red_btn
    sleep    3
    Input Text    name:phone    17766086297
    Input Password    name:password    123456
    Click Element    xpath:/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    sleep    5
    Click Element    /html/body/app-root/div/snail-menu-nav/div/a[2]
    Sleep    4
    Click Element    xpath:/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[1]/div[7]/a[1]
    Input Text    name:name    ${name}
    Input Text    name':phone    ${phone}
    Input Text    name:petName    ${animal}
    Click Element    class:red_btn
    Element Should Contain    xpath:/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[2]/table/tbody/tr/td[4]    ${phone}
    Close Browser
