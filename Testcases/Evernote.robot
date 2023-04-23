*** Settings ***
Library         ../Evernote/library/Evernote.py      WITH NAME       client1
Resource        ../Evernote/keywords/Evernote.robot
Suite Setup     Create Instance


*** Variables ***
${signup}     cheaderyeyvinnu4567@gmail.com
${signin}   opengfhwe1gggopen@gmail.com
${password}     Evernote@1
${task}         assignment
${dummy_text}   dummy_text
*** Keywords ***
Create Instance
    ${Client}=  Get Library Instance      client1
    Set Suite Variable      ${Client}
*** Test Cases ***
#I do signup, verify and signout
    #[Tags]    robot: skip
   # I do register account   ${Client}       ${email}      ${password}
   # I do verify account     ${Client}       ${email}
   # I do Signout account     ${Client}

I do signin with registred account and verify
   I do signin with registred account      ${Client}       ${signin}      ${password}
    I do verify_logged_user      ${Client}      ${signin}

I do create Task and verify
    I do create Task    ${Client}       ${task}     ${dummy_text}






