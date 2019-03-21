#! python3
#1401_csv_module.py - The csv Module

#THE CSV MODULE
#File -> example.csv

#CSV files are simple, lacking many of the features of an Excel spreadsheet. For example, CSV files
#•	 Don’t have types for their values—everything is a string
#•	 Don’t have settings for font size or color
#•	 Don’t have multiple worksheets
#•	 Can’t specify cell widths and heights
#•	 Can’t have merged cells
#•	 Can’t have images or charts embedded in them

#The advantage is simplicity

################
#READER OBJECTS#
################

#To read data from a CSV file with the csv module, you need to create a Reader
#object. A Reader object lets you iterate over lines in the CSV file. 

import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
#[['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'], ['4/6/
#2014 12:46', 'Pears', '14'], ['4/8/2014 8:59', 'Oranges', '52'], ['4/10/2014 2:0
#7', 'Apples', '152'], ['4/10/2014 18:10', 'Bananas', '23'], ['4/10/2014 2:40', '
#Strawberries', '98']]

#The most direct way to access the values in the Reader object is to convert it to a plain Python list by passing it to list()
#Using list() on this Reader object returns a list of lists, which you can store in a variable like exampleData.
#Now that you have the CSV file as a list of lists, you can access the value
#at a particular row and column with the expression exampleData[row][col],
#where row is the index of one of the lists in exampleData, and col is the index
#of the item you want from that list. 

print(exampleData[0][0])
#4/5/2014 13:34
print(exampleData[0][2])
#73
print(exampleData[1][1])
#Cherries
print(exampleData[6][1])
#Strawberries

exampleFile.close()

################################################
#Reading Data from Reader Objects in a for Loop#
################################################

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
exampleFile.close()
#Row #1 ['4/5/2014 13:34', 'Apples', '73']
#Row #2 ['4/5/2014 3:41', 'Cherries', '85']
#Row #3 ['4/6/2014 12:46', 'Pears', '14']
#Row #4 ['4/8/2014 8:59', 'Oranges', '52']
#Row #5 ['4/10/2014 2:07', 'Apples', '152']
#Row #6 ['4/10/2014 18:10', 'Bananas', '23']
#Row #7 ['4/10/2014 2:40', 'Strawberries', '98']

#After you import the csv module and make a Reader object from the
#CSV file, you can loop through the rows in the Reader object. Each row is
#a list of values, with each value representing a cell.
#The print() function call prints the number of the current row and the
#contents of the row. To get the row number, use the Reader object’s line_num
#variable, which contains the number of the current line.
#The Reader object can be looped over only once. To reread the CSV file,
#you must call csv.reader to create a Reader object.

################
#Writer Objects#
################
#A Writer object lets you write data to a CSV file. To create a Writer object, you
#use the csv.writer() function. 

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
#File:
#spam,eggs,bacon,ham
#"Hello, world!",eggs,bacon,ham
#1,2,3.141592,4

#On Windows, you’ll also need to pass a blank string for the open() function’s newline keyword argument. 
# if you forget to set the newline argument, the rows in output.csv will be double-spaced

####################################################
#The delimiter and lineterminator Keyword Arguments#
####################################################
#Say you want to separate cells with a tab character instead of a comma and
#you want the rows to be double-spaced. 
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
csvWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
csvWriter.writerow([1, 2, 3.141592, 4])
csvFile.close()
#spam	eggs	bacon	ham

#Hello, world!	eggs	bacon	ham

#1	2	3.141592	4

#Now that our cells are separated by tabs, we’re using the file extension
#.tsv, for tab-separated values.



