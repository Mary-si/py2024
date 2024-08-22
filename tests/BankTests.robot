*** Settings ***
Library    /Users/Mary/Documents/py2024/source/BankLibrary.py
Library    BuiltIn

*** Variables ***
${DEPOSIT_START_DATE}    08.09.2021
${DEPOSIT_END_DATE}      08.09.2025
${DEPOSIT_AMOUNT}        20000
${DEPOSIT_TERM_YEAR}     4
${PERCENT_DEPOSIT}       0.05

*** Test Cases ***
Test Deposit Creation
    ${deposit}=    Create Deposit    ${DEPOSIT_START_DATE}    ${DEPOSIT_END_DATE}
    Should Be Equal    ${deposit.deposit_start_date.strftime('%d.%m.%Y')}    ${DEPOSIT_START_DATE}
    Should Be Equal    ${deposit.end_date_deposit.strftime('%d.%m.%Y')}    ${DEPOSIT_END_DATE}

Test Bank Account Creation
    ${bank_account}=    Create Bank Account    ${DEPOSIT_AMOUNT}    ${DEPOSIT_TERM_YEAR}    ${PERCENT_DEPOSIT}
    Should Be Equal As Numbers    ${bank_account.deposit_amount}    ${DEPOSIT_AMOUNT}
    Should Be Equal As Numbers    ${bank_account.deposit_term_year}    ${DEPOSIT_TERM_YEAR}
    Should Be Equal As Numbers    ${bank_account.percent_deposit}    ${PERCENT_DEPOSIT}

Test Bank Account Calculation
    ${bank_account}=    Create Bank Account    ${DEPOSIT_AMOUNT}    ${DEPOSIT_TERM_YEAR}    ${PERCENT_DEPOSIT}
    ${final_amount}=    Calculate Final Amount    ${bank_account}
    Log    The final amount after ${DEPOSIT_TERM_YEAR} years is ${final_amount}
    ${expected_final_amount}=    Evaluate    round(${final_amount}, 2)
    Should Be Equal As Numbers    ${expected_final_amount}    24417.91
