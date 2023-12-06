*** Settings ***
Documentation     The Rescource file for Group 2. This file bridges the gap between,
...               our robot and the python file working selenium.
Library           Odoo_Keyword_Driven_Tests.py


*** Keywords ***
Connect to Server
    Open Connection
    Goto Odoo

Disconnect Server
    Cleanup Shutdown

Sleep
    [Arguments]     ${time_to_sleep}
    Pause to View   ${time_to_sleep}


Fill in Username and Password
    [Arguments]     ${Username}     ${Password}
    Text to Field   login          ${Username}
    Text to Field   password       ${Password}
    Click Button    Button