#! python3
#0711_combining_ignorecase_dotall_verbose.py - Combining re.IGNORECASE, re.DOT ALL , and re.VERBOSE

#What if you want to use re.VERBOSE to write comments in your regular expression
#but also want to use re.IGNORECASE to ignore capitalization? Unfortunately,
#the re.compile() function takes only a single value as its second argument. You
#can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and
#re.VERBOSE variables using the pipe character (|), which in this context is
#known as the bitwise or operator.

#So if you want a regular expression that’s case-insensitive and includes
#newlines to match the dot character, you would form your re.compile() call
#like this:

import re
someRegexValue = re.compile('foo', re.IGNORECASE|re.DOTALL)

#or

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

#MOre information bitwise operator: http://nostarch.com/automatestuff/
