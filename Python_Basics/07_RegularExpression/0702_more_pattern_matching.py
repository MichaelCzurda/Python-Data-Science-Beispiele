#! python3
#0702_more_pattern_matching.py - More Regex

#GROUPING WITH PARANTHESES
#Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).
#Then you can use the group() match object method to grab the matching
#text from just one group.

import re 

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My number is 415-555-4242.')

#The whole Match
print(mo.group(0))
#Group1
print(mo.group(1))
#Group2
print(mo.group(2))

#groups -> returns all groupsas tuple
print(mo.groups())


#MATCHING MULTIPLE GROUPS WITH THE PIPE
#The | character is called a pipe. You can use it anywhere you want to match one
#of many expressions.

heroRegex = re.compile(r'Batman|Tina Fey')
mo1=heroRegex.search('Batman and Tina Fey.')
#Batman
#When both occur, the first will be returned
print(mo1.group())

#Use prefix once
batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel')
print(mo.group())
#Batmobile
print(mo.group(1))
#mobile
print(mo.groups())
#('mobile',)


#OPTIONAL MATCHING WITH THE QUESTION MARK
#The ? character flags the group that precedes it as an optional part of the pattern.
batRegex=re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#'Batwoman'


#MATCHING ZERO OR MORE WITH THE STAR
#The * (called the star or asterisk) means “match zero or more”—the group
#that precedes the star can occur any number of times in the text.
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
#'Batwowowowoman'


#MATCHING ONE OR MORE WITH THE PLUS
#While * means “match zero or more,” the + (or plus) means “match one or more.”
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
#'Batwowowowoman'
mo1 = batRegex.search('The Adventures of Batman')
print(mo1 == None)


#MATCHING SPECIFIC REPETITIONS WITH CURLY BRACKET
#If you have a group that you want to repeat a specific number of times, 
#follow the group in your regex with a number in curly brackets. 
haRegex=re.compile(r'(Ha){3}')
mo1=haRegex.search('HaHaHa')
print(mo1.group())
#HaHaHa

mo2=haRegex.search('HaHa')
print(mo2==None)
#Instead of one number, you can specify a range by writing a minimum,
#a comma, and a maximum in between the curly brackets. For example, the
#regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
