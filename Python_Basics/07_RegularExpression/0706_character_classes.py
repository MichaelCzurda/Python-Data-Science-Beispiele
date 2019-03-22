#! python3
#0705_character_classes.py - Character Classes

#\d Any numeric digit from 0 to 9.

#\D Any character that is not a numeric digit from 0 to 9.

#\w Any letter, numeric digit, or the underscore character.
#(Think of this as matching “word” characters.)

#\W Any character that is not a letter, numeric digit, or the
#underscore character.

#\s Any space, tab, or newline character. (Think of this as
#matching “space” characters.)

#\S Any character that is not a space, tab, or newline.

import re

#Example:
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

#MAKING YOUR OWN CHARACTER CLASSES
#You can define your own character class using square brackets. For example, the character
#class [aeiouAEIOU] will match any vowel, both lowercase and uppercase. 

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#You can also include ranges of letters or numbers by using a hyphen -> [a-zA-Z0-9]

#Note that inside the square brackets, the normal regular expression
#symbols are not interpreted as such. This means you do not need to escape
#the ., *, ?, or () characters with a preceding backslash. For example, the
#character class [0-5.] will match digits 0 to 5 and a period. You do not need
#to write it as [0-5\.].

#By placing a caret character (^) just after the character class’s opening
#bracket, you can make a negative character class. A negative character class
#will match all the characters that are not in the character class.

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))
#['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

