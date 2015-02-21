Authentication:

1. To create new accessToken and secret key for a new user name:
	Go to: https://www.ihiredev.prateekchandan.me/admin

	username: demo
	password: ihiredev

	Click on AccessKeys, it will show you currently stored accesstokens and secret keys. 
	On right side, there is a button for adding new Access Tokens and secret keys

	It will popup a form and it will ask you for userId and it have already filled accessToken and secret Keys

2. For making authorized requests:
	
	In each request add the following headers:

	Authorization
	Date
	Userid
	accesstoken

	Date is current UTC timestamp in seconds
	Authorization is hmac_sha256_signature
	userid is the userid of user
	accesstoken is access token of user

	hmac_sha256_signature is calculated as hmac sha256 of the data
	Check this site for demo: http://www.freeformatter.com/hmac-generator.html

3. For verifying authentication, 
	Make a POST request on https://www.ihiredev.prateekchandan.me/input/add

	If you send an unauthenticated request then 