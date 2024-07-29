*** Settings ***
Library    ../BookUserLibrary.py
Library    BuiltIn

*** Variables ***
${USER_NAME}       John
${USER_SURNAME}    Doe
${USER_ID}         12345
${BOOK_TITLE}      Tree
${BOOK_AUTHOR}     Thomas Wyatt
${BOOK_PAGES}      180
${BOOK_ISBN}       978-5-06-002611-5

*** Test Cases ***
Test User Creation
    ${user}=    Create User    ${USER_NAME}    ${USER_SURNAME}    ${USER_ID}
    Should Be Equal    ${user.name}    ${USER_NAME}
    Should Be Equal    ${user.surname}    ${USER_SURNAME}

Test User Takes Book
    ${user}=    Create User    ${USER_NAME}    ${USER_SURNAME}    ${USER_ID}
    ${book}=    Create Book    ${BOOK_TITLE}    ${BOOK_AUTHOR}    ${BOOK_PAGES}    ${BOOK_ISBN}
    Take Book    ${user}    ${book}
    Should Be Equal    ${book.is_available}    ${False}
    Should Be Equal    ${user.took_book.title}    ${BOOK_TITLE}

Test User Returns Book
    ${user}=    Create User    ${USER_NAME}    ${USER_SURNAME}    ${USER_ID}
    ${book}=    Create Book    ${BOOK_TITLE}    ${BOOK_AUTHOR}    ${BOOK_PAGES}    ${BOOK_ISBN}
    Take Book    ${user}    ${book}
    Return Book    ${user}    ${book}
    Should Be Equal    ${book.is_available}    ${True}
    Should Be Equal    ${user.took_book}    ${None}

Test User Reserves Book
    ${user}=    Create User    ${USER_NAME}    ${USER_SURNAME}    ${USER_ID}
    ${book}=    Create Book    ${BOOK_TITLE}    ${BOOK_AUTHOR}    ${BOOK_PAGES}    ${BOOK_ISBN}
    Reserve Book    ${user}    ${book}
    Should Be Equal    ${book.is_reserved}    ${True}