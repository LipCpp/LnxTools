*** Settings ***
Library    ../window/exec.py

*** Variables ***
${path}    /home

*** Test Cases ***
Test functionality
    Call Add Path            ${path}
    Call Add Desktop File    1.0.0    TestApp    -    -    -    /bin/ls    false    /

*** Keywords ***
Call Add Path
    [Arguments]     ${txt}
    Add Path        ${txt}

Call Add Desktop File
    [Arguments]    ${version}    ${name}    ${comment}    ${genname}    ${keywords}    ${execute}    ${terminal}    ${icon}
    Add Desktop File    ${version}    ${name}    ${comment}    ${genname}    ${keywords}    ${execute}    ${terminal}    ${icon}