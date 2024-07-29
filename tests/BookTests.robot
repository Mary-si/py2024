*** Settings ***
Library    /Users/Mary/Documents/py2024/source/BookUserLibrary.py

*** Variables ***
${TITLE}      Title
${AUTHOR}     Author
${PAGES}      200
${ISBN}       123456789
${NAME}       John
${SURNAME}    Doe
${ID_NUMBER}  12345

*** Test Cases ***
Test Book Creation
    ${book}=    Create Book    ${TITLE}    ${AUTHOR}    ${PAGES}    ${ISBN}

Test Book Take
    ${user}=    Create User    ${NAME}    ${SURNAME}    ${ID_NUMBER}
    ${book}=    Create Book    ${TITLE}    ${AUTHOR}    ${PAGES}    ${ISBN}
    Take Book    ${user}    ${book}

Test Book Return
    ${user}=    Create User    ${NAME}    ${SURNAME}    ${ID_NUMBER}
    ${book}=    Create Book    ${TITLE}    ${AUTHOR}    ${PAGES}    ${ISBN}
    Take Book    ${user}    ${book}
    Return Book    ${user}    ${book}

Test Book Reservation
    ${user}=    Create User    ${NAME}    ${SURNAME}    ${ID_NUMBER}
    ${book}=    Create Book    ${TITLE}    ${AUTHOR}    ${PAGES}    ${ISBN}
    Reserve Book    ${user}    ${book}

*** Keywords ***
Create Book
    [Arguments]    ${title}    ${author}    ${pages}    ${isbn}
    ${book}=    BookUserLibrary.Create Book    ${title}    ${author}    ${pages}    ${isbn}
    RETURN    ${book}

Create User
    [Arguments]    ${name}    ${surname}    ${id_number}
    ${user}=    BookUserLibrary.Create User    ${name}    ${surname}    ${id_number}
    RETURN    ${user}

Take Book
    [Arguments]    ${user}    ${book}
    BookUserLibrary.Take Book    ${user}    ${book}

Return Book
    [Arguments]    ${user}    ${book}
    BookUserLibrary.Return Book    ${user}    ${book}

Reserve Book
    [Arguments]    ${user}    ${book}
    BookUserLibrary.Reserve Book    ${user}    ${book}
