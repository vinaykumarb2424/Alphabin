*** Settings ***
Library         ../Evernote/library/Evernote.py      WITH NAME       client1
Resource        ../Evernote/keywords/Evernote.robot
Suite Setup     Create Instance


*** Variables ***
${signup}     #venus6swamytemswer@gmail.com
${password}     Evernote@1
*** Keywords ***
Create Instance
    ${Client}=  Get Library Instance      client1
    Set Suite Variable      ${Client}
*** Test Cases ***
I do signup, verify and signout
   I do register account   ${Client}       ${signup}      ${password}
   I do verify account     ${Client}       ${signup}
   #I do Signout account     ${Client}





