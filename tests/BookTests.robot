*** Settings ***
Library    ../BookUserLibrary.py

*** Test Cases ***
Test Book Creation
    ${book}=    Create Book    Title    Author    200    123456789

Test Book Take
    ${user}=    Create User    John    Doe    12345
    ${book}=    Create Book    Title    Author    200    123456789
    Take Book    ${user}    ${book}

Test Book Return
    ${user}=    Create User    John    Doe    12345
    ${book}=    Create Book    Title    Author    200    123456789
    Take Book    ${user}    ${book}
    Return Book    ${user}    ${book}

Test Book Reservation
    ${user}=    Create User    John    Doe    12345
    ${book}=    Create Book    Title    Author    200    123456789
    Reserve Book    ${user}    ${book}