*** Settings ***
Library    ${CURDIR}/../../InfrastructureLibs/CreateDeviceSession.py
Library    ${CURDIR}/../../InfrastructureLibs/Parsers.py
Variables    ${CURDIR}/PlivoVariables.py

Suite Setup    Local Tb Parser
Test Setup    Open MyBrowser
Test Teardown    Close MyBrowser


*** Test Cases ***

Verify HomePage
	User Login    ${USERID}    ${USERPWD}
	Verify Loggedin User    ${USERID}
	Click Dashboard Navigation    Account
	Click Account Navigation    Payments
	Click Reedeem Coupon    ${WRONGCOUPON}    Incorrect
		
  	
*** Keywords ***

Open MyBrowser
    Open Browser    MyBrowser
	
Close MyBrowser
    Close Session
	