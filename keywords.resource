*** Settings ***
Documentation     The Rescource file for Group 2. This file bridges the gap between,
...               our robot and the python file working selenium.
Library           Odoo_Keyword_Driven_Tests.py


*** Variables ***
# Fake patient Data
# Name
${first_name}          Jenny
${middle_name}         franklyn
${Last_name}           Krueger
${cat_name}             Jenny Krueger 

# basic Info
${gender}              Female
${phone_number}        323-867-5309
${birthday}            02/12/1984
${email}               jenny.doe@gmail.com

# Address Info
${address}             1428 Elm Street
${city}                Fullerton
${pin_code}            1234

# Other Infor
${marital_status}      Married
${partner_name}        Freddy

# bad password error
${password_error}      Wrong login/password

${duplicate_error}      The operation cannot be completed


*** Keywords ***

Connect to Server
    Open Connection
    Sleep  .5
    Goto Odoo

Disconnect Server
    Cleanup Shutdown

Fill in Username and Password
    [Arguments]         ${Username}     ${Password}
    Text to Field       login           ${Username}
    Text to Field       password        ${Password}
    Click Button        /html/body/div[1]/main/div/div/div/form/div[3]/button

Click New Patient Button
    Sleep                1.5
    Click Button         /html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button

Fill in Patient Info
    Sleep   2
    Fill in Name
    Fill in Basic Info
    Fill in Address Info
    Fill in Other Info
    Sleep   1
    # to return to patient list
    Back

Verify Patient Info
    Sleep   1
    ${name_return}=      Get Field         name               ${cat_name}
    Verify              ${name_return}                        ${cat_name}

Fill in Name
    Text to Id          first_name          ${first_name}
    Text to Id          middle_name         ${middle_name}
    Text to Id          last_name           ${last_name}

Fill in Basic Info
    Select Dropdown     gender              ${gender}
    Text to Id          phone               ${phone_number}
    Text to Id          date_of_birth       ${birthday}
    Text to Id          email               ${email}

Fill in Address Info
    Text to Id          address             ${address}
    Text to Id          city                ${city}
    Text to Id          pin_code            ${pin_code}

Fill in Other Info
    Select Dropdown     marital_status      ${marital_status}
    # only needed when mairtal_status == married
    Text to Id          partner_name        ${partner_name}

Select Patient and Delete
    Check the Box   checkbox-comp-2
    Sleep   1
    Click Action then Delete

Verify Delete
    # just check for the name if its there throws an error.
    Not on Page     ${cat_name}

Check for Password Error
    Look for Error      ${password_error}

Check for Error
    Look for Error      ${duplicate_error}