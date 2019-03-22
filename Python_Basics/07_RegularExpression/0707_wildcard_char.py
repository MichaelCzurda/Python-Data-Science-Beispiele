#! python3
#0707_wildcard_char.py - The Wildcard Character

#. (dot) -> Wildcard Character -> match any character except newline

import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
#['cat', 'hat', 'sat', 'lat', 'mat']

#Remember that the dot character will match just one character, which
#is why the match for the text flat in the previous example matched only lat.
#To match an actual dot, escape the dot with a backslash: \.

#MATCH EVERYTHING WITH DOT-STAR

#For example, say you want to match the string 'First Name:', followed by 
#any and all text, followed by 'Last Name:', and then followed by anything again.

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
#Al
print(mo.group(2))
#Sweigart

#The dot-star uses greedy mode: It will always try to match as much text as
#possible. To match any and all text in a nongreedy fashion, use the dot, star,
#and question mark (.*?).

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
#<To serve man>

greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())
#<To serve man> for dinner.>


#MATCHING NEWLINES WITH THE DOT CHARACTER
#The dot-star will match everything except a newline. By passing re.DOTALL as
#the second argument to re.compile(), you can make the dot character match
#all characters, including the newline character.

noNewLineRegex = re.compile(r'.*')
print(noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
#Serve the public trust.

newLineRegex = re.compile(r'.*', re.DOTALL)
print(newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
#Serve the public trust.
#Protect the innocent.
#Uphold the law.
