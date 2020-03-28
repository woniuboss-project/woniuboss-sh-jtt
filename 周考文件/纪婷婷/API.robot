*** Settings ***
Library           RequestsLibrary
Resource          session

*** Variables ***
&{headers}        content-type=application/json
&{header}         content-type=application/x-www-form-urlencoded;charset=UTF-8

*** Test Cases ***
logintest
    [Template]    login
    15162629341    123456
    15162629341    1234

spendtest
    [Template]    spend
    1585324800    7    0    20
    1585324800    0    0    100

stockouttest
    [Template]    stockout
    2133552    17530    50    猫粮    500
    2133552    17530    10    狗粮    100

stockintest
    [Template]    stockin
    2133552    17530    50    猫粮    10    20
    2133552    17530    50    狗粮    5    5

*** Keywords ***
login
    [Arguments]    ${phone}    ${password}
    Create Session    session    https://snailpet.com
    ${body}    Create Dictionary    phone    ${phone}    password    ${password}
    ${resp}    Post Request    session    /v2/Passport/login    data=${body}    headers=${headers}
    Run Keyword If    ${resp.json()['error']}==1    Log    login_pass
    ...    ELSE    Log    login_fail

spend
    [Arguments]    ${actionTime}    ${type}    ${mark}    ${amount}
    Create Session    session    https://snailpet.com
    ${body}    Create Dictionary    phone=15162629341    password=123456
    Post Request    session    /v2/Passport/login    data=${body}    headers=${headers}
    ${data}    Create Dictionary    actionTime    ${actionTime}    type    ${type}    mark    ${mark}    amount    ${amount}    shopId    17530    shop_id    17530
    ${resp}    Post Request    session    /v2/Shop/addSpending    ${data}    headers=${header}
    Run Keyword If    ${resp.json()['error']}==1    Log    spend_pass
    ...    ELSE    Log    spend_fail

stockin
    [Arguments]    ${productId}    ${shopId}    ${number}    ${mark}    ${inPrice}    ${shelf_life}
    Create Session    session    https://snailpet.com
    ${body}    Create Dictionary    phone=15162629341    password=123456
    Post Request    session    /v2/Passport/login    data=${body}    headers=${headers}
    ${data}    Create Dictionary    productId    ${productId}    shopId    ${shopId}    number    ${number}    mark    ${mark}    inPrice    ${inPrice}    shelf_life    ${shelf_life}    production_time    null    exp_time
    ...    null    shop_id    17530
    ${resp}    Post Request    session    /v2/Shop/addSpending    ${data}    headers=${header}
    Run Keyword If    ${resp.json()['error']}==1    Log    stockin_pass
    ...    ELSE    Log    stockin_fail

stockout
    [Arguments]    ${productId}    ${shopId}    ${number}    ${mark}    ${out_of_price}
    Create Session    session    https://snailpet.com
    ${body}    Create Dictionary    phone=15162629341    password=123456
    Post Request    session    /v2/Passport/login    data=${body}    headers=${headers}
    ${data}    Create Dictionary    productId    ${productId}    shopId    ${shopId}    number    ${number}    mark    ${mark}    shelf_life    0    production_time    null    exp_time    null    out_of_price
    ...    ${out_of_price}    shop_id    17530
    ${resp}    Post Request    session    /v2/product/update/stocks    ${data}    headers=${header}
    Run Keyword If    ${resp.json()['error']}==1    Log    stockout_pass
    ...    ELSE    Log    stockout_fail
