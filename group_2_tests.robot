*** Settings ***
Documentation   A test suite for Odoo SaaS system
...             Keywords are imported from the resource file
Resource        keywords.resource
Default Tags    positive

*** Variables ***
${Username} = Get Value from User Input Username 
${Password} = Get Value from User Input Username

*** Notes_To_Me ***



*** Test Cases ***
Login User with Password
    Connect to Server
    Open Odoo
    Fill in Username and Password
    Sleep   3.5
    Disconnect Server