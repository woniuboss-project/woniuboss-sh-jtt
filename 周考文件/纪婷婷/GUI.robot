*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Logintest
    [Template]    login
    15162629341    123456    xpath:/html/body/app-root/snail-header/div/div/span/a    安全退出
    15162629341    123    xpath:/html/body/app-root/div/snail-index/div/div/div/div[2]/div[1]    登陆

edit_customer_test
    [Template]    edit_customer
    ss    13555556666    cat
    aa    13555556669    catcat

stocktest
    [Template]    stockin
    123456    猫粮
    123457    猫粮

inventorytest
    [Template]    inventory
    100
    200

stockouttest
    [Template]    stockout
    10
    20

*** Keywords ***
login
    [Arguments]    ${phone}    ${password}    ${xpath}    ${expect}
    Open Browser    https://snailpet.com/index
    Click Element    class:red_btn
    Input Text    name:phone    ${phone}
    Input Password    name:password    ${password}
    Click Element    class:ori-btn
    Wait Until Element Is Visible    ${xpath}
    Element Should Contain    ${xpath}    ${expect}
    Close Browser

edit_customer
    [Arguments]    ${cname}    ${cphone}    ${animal}
    Open Browser    https://snailpet.com/index
    Click Element    class:red_btn
    Input Text    name:phone    15162629341
    Input Password    name:password    123456
    Click Element    class:ori-btn
    Sleep    5
    Click Element    xpath:/html/body/app-root/div/snail-menu-nav/div/a[2]/div[1]
    Sleep    5
    Click Element    css=div.screen-edit-btn-new:nth-child(7) > a:nth-child(2)
    Sleep    10
    Input Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/input    ${cname}
    Sleep    10
    Input Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/input    ${cphone}
    Sleep    10
    Input Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[2]/div/div[2]/ul/li/div[1]/div[1]/div/div/input    ${animal}
    Sleep    10
    Click Element    css=div.pop_window:nth-child(1) > div:nth-child(3) > div:nth-child(2)
    Element Should Contain    css=.body > td:nth-child(10) > a:nth-child(4)    删除
    Close Browser

stockin
    [Arguments]    ${barcode}    ${goodsname}
    Open Browser    https://snailpet.com/index
    Click Element    class:red_btn
    Input Text    name:phone    15162629341
    Input Password    name:password    123456
    Click Element    class:ori-btn
    Sleep    5
    Click Element    xpath:/html/body/app-root/div/snail-menu-nav/div/a[3]/div[1]
    Sleep    15
    Click Element    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[2]/div[1]/a[1]
    Sleep    15
    Input Text    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[5]/div/div/div[2]/div/div[3]/div[1]/div/div/input    ${barcode}
    Sleep    15
    Input Text    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[5]/div/div/div[2]/div/div[4]/div[1]/div/div/input    ${goodsname}
    Sleep    15
    Click Element    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[5]/div/div/div[2]/div/div[7]/div/label
    Sleep    15
    Click Element    xpath=/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[5]/div/div/div[2]/div/div[7]/div/div/div/ul/li[1]
    Sleep    10
    Click Element    xpath=/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[5]/div/div/div[3]/div[2]
    Sleep    10
    Element Should Contain    xpath=/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[3]/table/tbody/tr/td[8]/a[5]/span/span[1]    下架
    Close Browser

inventory
    [Arguments]    ${Q}
    Open Browser    https://snailpet.com/index
    Click Element    class:red_btn
    Input Text    name:phone    15162629341
    Input Password    name:password    123456
    Click Element    class:ori-btn
    Sleep    5
    Click Element    xpath:/html/body/app-root/div/snail-menu-nav/div/a[3]/div[1]
    Sleep    15
    Click Element    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[3]/table/tbody/tr/td[8]/a[1]
    Sleep    15
    Input Text    css:#idIconInput > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)    ${Q}
    Sleep    19
    Click Element    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[7]/div/div/div[3]/div[2]
    Element Should Contain    xpath=/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[3]/table/tbody/tr/td[8]/a[5]/span/span[1]    下架
    Close Browser

stockout
    [Arguments]    ${outQ}
    Open Browser    https://snailpet.com/index
    Click Element    class:red_btn
    Input Text    name:phone    15162629341
    Input Password    name:password    123456
    Click Element    class:ori-btn
    Sleep    5
    Click Element    xpath:/html/body/app-root/div/snail-menu-nav/div/a[3]/div[1]
    Sleep    15
    Click Element    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[3]/table/tbody/tr/td[8]/a[2]
    Sleep    30
    Input Text    xpath=/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[8]/div/div/div[2]/div/div[1]/div/div/input    ${outQ}
    Sleep    20
    Click Element    xpath:/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[8]/div/div/div[3]/div[2]
    Element Should Contain    xpath=/html/body/app-root/div/ng-component/div/div/snail-product-stock/div[3]/table/tbody/tr/td[8]/a[5]/span/span[1]    下架
    Close Browser
