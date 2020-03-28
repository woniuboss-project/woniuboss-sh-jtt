*** Settings ***
Library           Selenium2Library

*** Test Cases ***
woniuxiaodian
    [Tags]
    [Template]    woniuxiaodian
    13817405021    000000    李安    13817678988    mao    狗
    13817405021    111111    李安    13817678988    mao    狗
    13817405021    000000    @@@    13817678999    mao    狗

*** Keywords ***
woniuxiaodian
    [Arguments]    ${phone}    ${password}    ${name}    ${customerphone}    ${animalname}    ${goods}
    Open Browser    https://snailpet.com/index    Firefox
    sleep    2
    Click Element    class=white_btn
    sleep    3
    Input Text    name=phone    ${phone}
    Input Password    name=password    ${password}
    Click Element    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Wait Until Element Is Visible    id=shop_name
    Element Should Contain    id=shop_name    哥斯拉简并态小店
    sleep    5
    Click Element    xpath=/html/body/app-root/div/snail-menu-nav/div/a[2]/div[1]
    sleep    15
    Click Element    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[1]/div[7]/a[1]
    Input Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/input    ${name}
    Input Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/input    ${customerphone}
    Input Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[2]/div/div[2]/ul/li/div[1]/div[1]/div/div/input    ${animalname}
    Click Element    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[3]/div[2]
    Element Should Contain    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[2]/table/tbody/tr/td[10]/a[5]    详情
    sleep    10
    Click Element    xpath=/html/body/app-root/div/snail-menu-nav/div/a[5]/div[1]
    sleep    5
    Input Text    xpath=//*[@id="idInputCrux"]    ${goods}
    Element Should Contain    xpath=/html/body/app-root/div/snail-else-main/snail-sale/div[1]/div[2]/table/tbody/tr[2]/td[1]/a    ${goods}
    Click Element    xpath=/html/body/app-root/div/snail-menu-nav/div/a[1]/div[1]
    sleep    4
    Click Element    xpath=/html/body/app-root/div/snail-cash-main/snail-cash/div[1]/div/div[3]/a/div
    Element Should Contain    xpath=/html/body/app-root/div/snail-cash-main/snail-cash-pay/div[1]/div/div/div/div/div[1]/div/button    订单权益
    sleep    10
    Click Element    xpath=/html/body/app-root/div/snail-menu-nav/div/a[7]
    sleep    2
    Click Element    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-nav/div/a[2]
    Element Should Contain    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-member/div/ul/li[6]/div    会员次卡
    sleep    2
    Click Element    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-nav/div/a[3]
    Element Should Contain    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-sale/div/div/ul/li[1]/span[1]    商品价值
    sleep    2
    Click Element    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-nav/div/a[4]
    Element Should Contain    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-clerk/div/ul/li[1]/h3    合计总销售：￥
    sleep    2
    Click Element    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-nav/div/a[5]
    Element Should Contain    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-clerk/div[1]/div/table/tbody/tr/td[9]/a[2]    发工资
    sleep    2
    Click Element    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-nav/div/a[6]
    Element Should Contain    xpath=/html/body/app-root/div/snail-chart-main/div/snail-chart-pay/div/ul/li[4]    合计
    Close Browser
    [Teardown]
