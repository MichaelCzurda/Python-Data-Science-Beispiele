#! python3
#0704_findall_Method.py - Findall

#search -> return first matched text
#findall -> return strings of every match

import re

#search
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
#415-555-9999

#findall -> list of strings with match - as long as there are no groups in the regular expression
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#['415-555-9999', '212-555-0000']


#If there are groups in the regular expression, then findall() will return
#a list of tuples. Each tuple represents a found match, and its items are the
#matched strings for each group in the regex.

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#[('415', '555', '9999'), ('212', '555', '0000')]
