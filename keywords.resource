*** Settings ***
Documentation     The Rescource file for Group 2. This file bridges the gap between,
...               our robot and the python file working selenium.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           Odoo_Keyword_Driven_Tests.py


*** Keywords ***
Connect to Server
    Open Connection

Disconnect Server
    Cleanup Shutdown

Sleep
    [Arguments]     ${time_to_sleep}
    Pause to View   ${time_to_sleep}

Open Odoo
    Goto Odoo

Click Button
    [Arguments]    ${button_name}
    Click Button