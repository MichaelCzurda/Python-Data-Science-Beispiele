#! python3
#0705_caret_dollar_sign.py - The Caret and Dollar Sign Characters

#You can also use the caret symbol (^) at the start of a regex to indicate that
#a match must occur at the beginning of the searched text. Likewise, you can
#put a dollar sign ($) at the end of the regex to indicate the string must end
#with this regex pattern. And you can use the ^ and $ together to indicate
#that the entire string must match the regex—that is, it’s not enough for a
#match to be made on some subset of the string.

import re

#Example:
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello World!'))
#<re.Match object; span=(0, 5), match='Hello'>
print(beginsWithHello.search('He said hello.') == None)
#True

#The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
#<re.Match object; span=(16, 17), match='2'>
print(endsWithNumber.search('Your number is forty two.') == None)
#True


#The r'^\d+$' regular expression string matches strings that both begin
#and end with one or more numeric characters.

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
#<re.Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890') == None)
#True
print(wholeStringIsNum.search('12 34567890') == None)
#True

#The last two search() calls in the previous interactive shell example demonstrate
#how the entire string must match the regex if ^ and $ are used.
