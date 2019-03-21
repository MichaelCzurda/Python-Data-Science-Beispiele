#!python3
#0904_project_rename_amer_euro.py - Project: Renaming Files with American-Style Dates to European-Style Dates

#Problem:
#thousand of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to Europeanstyle dates (DD-MM-YYYY)

#Here’s what the program does:
#•	 It searches all the filenames in the current working directory for
#		American-style dates.
#•	 When one is found, it renames the file with the month and day swapped
#		to make it European-style.

#This means the code will need to do the following:
#•	 Create a regex that can identify the text pattern of American-style dates.
#•	 Call os.listdir() to find all the files in the working directory.
#•	 Loop over each filename, using the regex to check whether it has a date.
#•	 If it has a date, rename the file with shutil.move().

#################################################
#Step 1: Create a Regex for American-Style Dates#
#################################################

import re, os, shutil

datepattern = re.compile(r"""^(.*?) 	#all text before the date
((0|1)?\d)-							#one or two digits for the month
((0|1|2|3)?\d)-						#one or two digits for the day
((19|20)\d\d)						#four digits for the year
(.*?)$
""", re.VERBOSE)

####################################################
#Step 2: Identify the Date Parts from the Filenames#
#Step 3: Form the New Filename and Rename the Files#
####################################################

for amerFilename in os.listdir('.'):
	mo=datepattern.search(amerFilename)
#Step2
	# Skip files without a date.
	if mo == None:
		continue
		
	# Get the different parts of the filename.
	#print(mo.groups())
	#('sers_', '03', '0', '06', '0', '2018', '20', '.txt')
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

#Step3	
	# Form the European-style filename.
	new_name = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
	
	# Get the full, absolute file paths.
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	europFilename = os.path.join(absWorkingDir, new_name)

	#Rename the file
	print('Renaming {} to {}...'.format(amerFilename, europFilename))
	shutil.move(amerFilename, europFilename)


#Ideas for similar programs
#There are many other reasons why you might want to rename a large number of files.
#•	 To add a prefix to the start of the filename, such as adding spam_ to
#		rename eggs.txt to spam_eggs.txt
#•	 To change filenames with European-style dates to American-style dates
#•	 To remove the zeros from files such as spam0042.txt
