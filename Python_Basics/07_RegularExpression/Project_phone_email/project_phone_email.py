#! python3
#0713_project_phone_email.py - Project: Phone Number and Email Address Extractor

#finding every phone number and email address in a long web page or document.
#search in copied text in clibboard
#replace text in clipboard with just phone numbers and email adresses

#Before coding get big picture of what to do:
#Steps:
#• Get the text off the clipboard.
#• Find all phone numbers and email addresses in the text.
#• Paste them onto the clipboard.

#how thsi might work in code - Roadmap:
#• Use the pyperclip module to copy and paste strings.
#• Create two regexes, one for matching phone numbers and the other for matching email addresses.
#• Find all matches, not just the first match, of both regexes.
#• Neatly format the matched strings into a single string to paste.
#• Display some kind of message if no matches were found in the text.

#Step 1: Create a Regex for Phone Numbers

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?	#area code
(s|-|\.)?			#seperator
(\d{3})				#first 3 digits
(s|-|\.)			#seperator
(\d{4})				#last 4 digits
(\s(ext|x|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)

#The phone number begins with an optional area code, so the area code
#group is followed with a question mark. Since the area code can be just
#three digits (that is, \d{3}) or three digits within parentheses (that is, \(\d{3}\)),
#you should have a pipe joining those parts. You can add the regex comment
## Area code to this part of the multiline string to help you remember what
#(\d{3}|\(\d{3}\))? is supposed to match.
#The phone number separator character can be a space (\s), hyphen (-),
#or period (.), so these parts should also be joined by pipes. The next few
#parts of the regular expression are straightforward: three digits, followed
#by another separator, followed by four digits. The last part is an optional
#extension made up of any number of spaces followed by ext, x, or ext., followed
#by two to five digits.

# STep 2: Regex for Email

emailRegex=re.compile(r'''(
[a-zA-Z0-9._%+-]+		#username
@						# @ symbol
[a-zA-Z.-]+				#domain name
(\.[a-zA-Z]{2,4})		#dot-something
)''', re.VERBOSE)

#username one or more character
#then seperator @
#domain, only letters, numbers, periods and hyphens
#last the dotcom part(top-level domain)

#Step 3: Final All Matches in the Clipboard Text

text = str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
	#bring phone numbers to satndard format
	print(groups)
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' +groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

#There is one tuple for each match, and each tuple contains strings for
#each group in the regular expression. Remember that group 0 matches the
#entire regular expression, so the group at index 0 of the tuple is the one you
#are interested in.
	
# Step 4: Join the Matches into a String for the Clipboard

#pyperclip.copy() takes one string as argument and not list of strings -> join

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
	
#Ideas for similar programm:
#website URLS
#clean up dates -> to standard format
#remove sensitive information from text (SVN, Kreditkarte, etc.)
#find typos and replace them -> multiple spaces, repeated words, multiple exclamation marks 
