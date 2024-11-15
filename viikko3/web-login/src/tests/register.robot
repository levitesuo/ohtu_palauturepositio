*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pasi
    Set Matching Passwords  123456789
    Submit Credentials
    Registeration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pa
    Set Matching Passwords  123456789
    Submit Credentials
    Registeration Should Fail
# ...

Register With Valid Username And Too Short Password
    Set Username  pasi
    Set Matching Passwords  12
    Submit Credentials
    Registeration Should Fail
# ...

Register With Valid Username And Invalid Password
    Set Username  pasi
    Set Matching Passwords  abcdefghijklmn
    Submit Credentials
    Registeration Should Fail
# salasana ei sisällä halutunlaisia merkkejä
# ...

Register With Nonmatching Password And Password Confirmation
    Set Username  pasi
    Set Password  123456789
    set Confirmation Password  1234567890
    Submit Credentials
    Registeration Should Fail
# ...

Register With Username That Is Already In Use
    Set Username  kalle
    Set Matching Passwords  123456789
    Submit Credentials
    Registeration Should Fail
#

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Matching Passwords
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Set Confirmation Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Registeration Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Registeration Should Fail
    Title Should Be  Register
#...