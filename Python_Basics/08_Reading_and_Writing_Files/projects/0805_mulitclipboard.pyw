#! python3
#0805_mulitclipboard.pyw - Project: Multiclipboards

# Usage: 	py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# 			py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# 			py.exe mcb.pyw list - Loads all keywords to clipboard.

#If you have several different pieces of text that you need to copy and paste, you have to keep highlighting 
#and copying the same few things over and over again. You can write a Python program to keep track of multiple pieces of text.

#The name of the File is 0805_mulitclipboard.pyw
#The .pyw extension means that Python won’t showa Terminal window when it runs this program. 

#Program:
#The program will save each piece of clipboard text under a keyword.
#For example, when you run py "0805_mulitclipboard.pyw save spam", the current contents of the
#clipboard will be saved with the keyword spam. This text can later be loaded
#to the clipboard again by running py mcb.pyw spam. And if the user forgets
#what keywords they have, they can run py mcb.pyw list to copy a list of all
#keywords to the clipboard.

#Here’s what the program does:
#•	 The command line argument for the keyword is checked.
#•	 If the argument is save, then the clipboard contents are saved to the keyword.
#•	 If the argument is list, then all the keywords are copied to the clipboard.
#•	 Otherwise, the text for the keyword is copied to the keyboard. 

#This means the code will need to do the following:
#•	 Read the command line arguments from sys.argv.
#•	 Read and write to the clipboard.
#•	 Save and load to a shelf file.

#Further ToDo:
# creating a batch file named mcb.bat with the following content to run script from the Run. Content:
#	@pyw.exe C:\Users\michaelc.AITC\Documents\Python Scripts\ATBS\08_Reading_and_Writing_Files\projects\0805_mulitclipboard.pyw %*

##################################
#Step 1: Comments and Shelf Setup#
##################################

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

####################################################
#Step 2: Save Clipboard Content with a keyword     #
#Step 3: List Keyword and Load a Keywords's Content#
####################################################

#Step 2
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[str(sys.argv[2])] == pyperclip.paste()
#Step 3
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		
mcbShelf.close()

