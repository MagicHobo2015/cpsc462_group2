*** Settings ***
Documentation   A test suite for Odoo SaaS system
...             This is where test cases originate
Resource        keywords.resource
Default Tags    positive

*** Variables ***
${Username}  odoo15
# bad practice, dont do this.
${Password}     @test1

*** Test Cases ***
# Since everything starts with loging in, this is an excelent first test.
# Test Case 1
Login User with Password
    Connect to Server
    Fill in Username and Password    ${Username}    ${Password}
    Disconnect Server

# Test Case 2 - 
Create New Patient
    Connect to Server
    Fill in Username and Password       ${Username}     ${Password}
    Click New Patient button
    Fill in Patient Info
    Verify Patient Info
    Disconnect Server

# Test Case 3 -
Delete Patient
    Connect to Server
    Fill in Username and Password    ${Username}    ${Password}
    Sleep   2
    Select Patient