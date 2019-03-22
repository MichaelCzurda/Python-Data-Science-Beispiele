#! python3
#0701_regex.py - An insecure password locker programm


#1. Import the regex module with import re.
import re

#2. Create a Regex object with the re.compile() function. (Remember to use a
#raw string so don't need to escape backslahes.)
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

#3. Pass the string you want to search into the Regex object’s search() method.
#This returns a Match object.
mo = phoneNumRegex.search('My number is 455-555-4242.')

#4. Call the Match object’s group() method to return a string of the actual
#matched text.
print('Phone Number found: '+mo.group())


#Regex tester at http:// regexpal.com/
