*** Settings ***

Documentation     Keywords supported for evernote Application to test testcases

*** Keywords ***
I do register account
    [Arguments]    ${Client}      ${email}     ${password}
    Call Method    ${Client.signup}        click_signup_for_free
    Call Method    ${Client.signup}    click_free_account
    Call Method    ${Client.signup}    fill_details   ${email}     ${password}
    Call Method    ${Client.signup}    click_continue
    Call Method    ${Client.signup}    verify_signup
    #[Return]    ${result}
I do setup account
    [Arguments]    ${Client}      ${email}
    Call Method    ${Client.home}    make_setup
    #Call Method    ${Client.home}    click_get_started
    #Call Method    ${Client.home}    choose_category
I do Signout account
    [Arguments]    ${Client}
    Call Method    ${Client.home}    sign_out

I do signin with registred account
    [Arguments]    ${Client}      ${email}      ${password}
    Call Method    ${Client.login}    click_login_link
    Call Method    ${Client.login}    enter_email       ${email}
    Call Method    ${Client.login}    click_continue
    Call Method    ${Client.login}    enter_password        ${password}
    Call Method    ${Client.login}    click_signin

I do verify_logged_user
    [Arguments]    ${Client}    ${email}
    Call Method    ${Client.home}       verify_logged_user  ${email}

I do create Task
    [Arguments]    ${Client}    ${task}     ${dummy_text}
    Call Method    ${Client.task}       click_task
    Call Method    ${Client.task}       create_task     ${task}
    #Call Method    ${Client.task}       open_created_task
    Call Method    ${Client.task}       click_notes_tab  #open_notes
    Call Method    ${Client.task}       open_insert
    Call Method    ${Client.task}       add_table       ${dummy_text}


