
#! python3
#04_strings_passwordLocker.py - An insecure password locker programm

import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
 'luggage': '12345'}
 
 
#Handle Command LIne Arguments

if len(sys.argv) <2:
	print('Usage: python 04_strings_passwordLocker.py [account] - copy account password')
	sys.exit()
	
account = sys.argv[1] #first cammnd line arg is the account name


#Copy the Right Password
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)

