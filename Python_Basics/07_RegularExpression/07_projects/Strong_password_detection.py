#!python3
#strong_password_detection.py - Strong Password Detection

import re

def checkpwd(passwd):
	errors = []
	number = re.compile(r'\d+')
	upper = re.compile(r'[A-Z]+')
	lower = re.compile(r'[a-z]')
	if number.search(passwd) ==  None:
		errors.append('The password should contain a number!')
	if upper.search(passwd) == None:
		errors.append('The password should contain an uppercase letter!')
	if lower.search(passwd) == None:
		errors.append('The password should contain a lowercase letter!')
	if len(passwd) < 8:
		errors.append('The password should be at least eight characters long!')
	if errors:
		return errors
	else:
		errors.append('The password is safe')
		return errors
		
passwd = 'heL1oooo'
for i in checkpwd(passwd):
	print(i)
	


