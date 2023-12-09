*** Settings ***
Documentation   A test suite for Odoo SaaS system
...             This is where test cases originate
Resource        keywords.resource
Default Tags    Positive

*** Variables ***
${Username}  odoo15
# bad practice, dont do this.
${Password}     @test1
${bad_password}     @test2

*** Test Cases ***
# Since everything starts with loging in, this is an excelent first test.
# Test Case 1
Login User with Password
    Connect to Server
    Fill in Username and Password    ${Username}    ${Password}
    Sleep   1.5
    Disconnect Server

# Test Case 2 - 
Create New Patient
    Connect to Server
    Fill in Username and Password       ${Username}     ${Password}
    Sleep   1.5
    Click New Patient Button
    Fill in Patient Info
    Verify Patient Info
    Disconnect Server

#   Test Case 3 -
Delete Patient
    Connect to Server
    Fill in Username and Password    ${Username}    ${Password}
    Sleep   1.5
    Select Patient and Delete
    Verify Delete
    Disconnect Server

#   Test Case 4 -
Attempt Login Bad Password
    [Tags]  Negative
    Connect to Server
    Fill in Username and Password   ${Username}     ${bad_password}
    Sleep   1.5
    Check for Password Error
    Disconnect Server

#   Test Case 5 -
Add Duplicate Patient
    [Tags]  Negative
    Connect to Server
    Fill in Username and Password   ${Username}     ${Password}
    Sleep   1.5
    Click New Patient Button
    Fill in Patient Info
    Sleep   1.5
    Click New Patient Button
    Sleep   1.5
    Fill in Patient Info
    # check for the error
    Check for Error
    Disconnect Server