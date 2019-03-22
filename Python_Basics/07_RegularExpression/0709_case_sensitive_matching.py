#! python3
#0709_case_sensitive_matching.py - Case-Insensitive Matching

#Normally, regular expressions match text with the exact casing you specify.
#But sometimes you care only about matching the letters without worrying
#whether they’re uppercase or lowercase. To make your regex case-insensitive,
#you can pass re.IGNORECASE or re.I as a second argument to re.compile().

import re
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
#RoboCop

print(robocop.search('ROBOCOP protects the innocent.').group())
#ROBOCOP

