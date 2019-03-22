#! python3
#05_adding_bullets_wiki.py - Add Bullets to List in Clipboard

#The script will get the text from the clipboard, add
#a star and space to the beginning of each line, and then paste this new
#text to the clipboard.

import pyperclip

text = pyperclip.paste()
#new line seperated string

#Separate the Lines of Text and Add the Star
lines = []
for line in text.split('\n'):
	lines.append('* '+str(line))

#Join the Modified Lines

text = '\n'.join(lines)
pyperclip.copy(text)

