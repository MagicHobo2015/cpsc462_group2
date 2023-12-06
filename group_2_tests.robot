*** Settings ***
Documentation   A test suite for Odoo SaaS system
...             This is where test cases originate
Resource        keywords.resource
Default Tags    positive

*** Variables ***
${Username}  odoo15
# bad practice, dont do this.
${Password}  @test1

*** Notes_To_Me ***
# this section works as a block comment, mostly for notes.
# Username and Password Come from User Input

*** Test Cases ***
# Since everything starts with loging in, this is an excelent first test.
# Test Case 1
Login User with Password
    Connect to Server
    Fill in Username and Password    ${Username}    ${Password}
    Sleep   3.5
    Disconnect Server

# Test Case 2

