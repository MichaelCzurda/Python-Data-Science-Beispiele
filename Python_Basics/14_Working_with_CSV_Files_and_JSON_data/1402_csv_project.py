#! python3
#1402_csv_project.py - Project: Removing the Header from CSV Files

#Say you have the boring job of removing the first line from several hundred
#CSV files. Maybe you’ll be feeding them into an automated process that
#requires just the data and not the headers at the top of the columns. You
#could open each file in Excel, delete the first row, and resave the file—but
#that would take hours. Let’s write a program to do it instead.

#The program will need to open every file with the .csv extension in the
#current working directory, read in the contents of the CSV file, and rewrite
#the contents without the first row to a file of the same name. This will
#replace the old contents of the CSV file with the new, headless contents.

#WARNING
#As always, whenever you write a program that modifies files, be sure to back up the
#files, first just in case your program does not work the way you expect it to. You don’t
#want to accidentally erase your original files.

#At a high level, the program must do the following:
#•	 Find all the CSV files in the current working directory.
#•	 Read in the full contents of each file.
#•	 Write out the contents, skipping the first line, to a new CSV file.

#At the code level, this means the program will need to do the following:
#•	 Loop over a list of files from os.listdir(), skipping the non-CSV files.
#•	 Create a CSV Reader object and read in the contents of the file, using
#		the line_num attribute to figure out which line to skip.
#•	 Create a CSV Writer object and write out the read-in data to the new file.

######################################################
#Step1: Loop Through Each CSV File					 #
#Step 2: Read in the CSV File	  					 #
#Step 3: Write Out the CSV File Without the First Row#
######################################################

import os, csv

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
#Step 1
for csvFile in os.listdir('.'):
	if not csvFile.endswith('.csv'):
		continue
	#Step 2
	print('Removing header from ' + csvFile + '...')
	csvRows = []
	csvFileObj = open(csvFile)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue #skip first row
		else:
			csvRows.append(row)
	csvFileObj.close()
	#Step 3
	csvFileObj = open(os.path.join('headerRemoved', csvFile), 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()

#Ideas for Similar Programs
#The programs that you could write for CSV files are similar to the kinds you
#could write for Excel files, since they’re both spreadsheet files. You could
#write programs to do the following:
#•	 Compare data between different rows in a CSV file or between multiple CSV files.
#•	 Copy specific data from a CSV file to an Excel file, or vice versa.
#•	 Check for invalid data or formatting mistakes in CSV files and alert the user to these errors.
#•	 Read data from a CSV file as input for your Python programs.
