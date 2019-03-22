#!python3
#regex_strip_func.py - Regex Version of strip()

import re

def strip_regex(text, char=' '):
	charJoin = r'['+char+']*([^'+char+'].*[^'+char+'])['+char+']*'
	cRegex = re.compile(charJoin, re.DOTALL)
	return cRegex.search(text).group(1)


print(strip_regex(text='   dfdff  sdd  '))
print(strip_regex(text='####dfdff###sdd######', char='#'))
