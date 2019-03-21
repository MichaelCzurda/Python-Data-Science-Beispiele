#! python3
#0803_file_reading_writing.py - The File Reading/Writing Process

#Next secrtions will cover normal textfiles
#Text files with the .txt extension or Python script files with the .py extension are examples of plaintext files.

#Binary files are all other file types, such as word processing documents, PDFs, images, spreadsheets, 
#and executable programs. If you open a binary file in Notepad or TextEdit, it will look like scrambled nonsense

#There are three steps to reading or writing files in Python.
#1. Call the open() function to return a File object.
#2. Call the read() or write() method on the File object.
#3. Close the file by calling the close() method on the File object.

########################################
#OPENING FILES WITH THE open() FUNCTION#
########################################
#open() function -> pass it a string path indicating the file you want to open

#manually created file hello.txt
import os
print(os.getcwd())
#C:\Users\michaelc.AITC\Documents\Python Scripts\ATBS\08_Reading_and_Writing_Files

helloFile = open(os.path.join(os.getcwd(),'hello.txt'))
#opens file in read mode (standard) -> you can only read
#explicit read -> open(file, 'r')
#returns File Object

###########################
#READING CONTENTS OF FILE'#
###########################
helloContent = helloFile.read()
print(helloContent)
#Hello world!

#If you think of the contents of a file as a single large string value, the
#read() method returns the string that is stored in the file.

#readlines() method to get a list of string values from the file, one string for each line of text. 
#add manually lines to sonet29.txt
sonnetFile = open(os.path.join(os.getcwd(),'sonnet29.txt'))
print(sonnetFile.readlines())
#[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
#outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
#look upon myself and curse my fate,']

#Note that each of the string values ends with a newline character, \n , except for the last line of the file

###############
#WRITING FILES#
###############
#can't write to file in read mode
#open in "write plaintext mode" or "append plaintext mode"
#write -> overwrites file
#append -> append text to file

#After reading or writing a file, call the close() method before opening the file again.
#write, create file
baconfile = open('bacon.txt', 'w')
baconfile.write('Hello World!\n')

baconfile.close()
#append text
baconfile = open('bacon.txt', 'a')
baconfile.write('Bacon is not a vegetable.')

baconfile.close()
baconfile = open('bacon.txt')
#read content
content = baconfile.read()
baconfile.close()
print(content)

#########################################
#Saving Variables with the shelve Module#
#########################################
#You can save variables in your Python programs to binary shelf files using the shelve module
#This way, your program can restore data to variables from the hard drive.

#Example ->  if you ran a program and entered some configuration settings, you could save those 
#settings to a shelf file and then have the program load them the next time it is run.

#Example
import shelve
shelveFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelveFile['cats'] = cats
shelveFile.close()
#Call shelve.open() and pass it a filename, and then store the returned shelf value in a variable. 
#You can make changes to the shelf value as if it were a dictionary.
#When you’re done, call close() on the shelf value. 
#Three new files:
#	mydata.bak 
#	mydata.dat
#	mydata.dir
#OnOS X, only a single mydata.db file will be created.

#The module frees you from worrying about how to store your program’s data to a file.
#Your programs can use the shelve module to later reopen and retrieve the data from these 
#shelf files. Shelf values don’t have to be opened in read or write mode—they can do both once opened.

shelveFile = shelve.open('mydata')
print(type(shelveFile))
#<class 'shelve.DbfilenameShelf'>
print(shelveFile['cats'])
#['Zophie', 'Pooka', 'Simon']
shelveFile.close()
#Entering shelfFile['cats'] returns the same list that we stored earlier

#Just like dictionaries, shelf values have keys() and values() methods that
#will return list-like values of the keys and values in the shelf. Since these
#methods return list-like values instead of true lists, you should pass them
#to the list() function to get them in list form. 
shelveFile=shelve.open('mydata')
print(list(shelveFile.keys()))
#['cats']
print(list(shelveFile.values()))
#[['Zophie', 'Pooka', 'Simon']]
shelveFile.close()

#####################################################
#Saving Variables with the pprint.pformat() Function#
#####################################################
#the pprint.pprint() function will “pretty print” the contents of a list or dictionary to the screen,
#while the pprint.pformat() function will return this same text as a string instead of printing it.
#Not only is this string formatted to be easy to read, but it is also syntactically correct Python code.

#Using pprint.pformat() will give you a string that you can write to .py file. 
#This file will be your very own module that you can import whenever you want to use the variable stored in it.
import pprint
cats =  [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
#[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' +  pprint.pformat(cats) + '\n')
fileObj.close()
#The modules that an import statement imports are themselves just Python scripts. When the string from 
#pprint.pformat() is saved to a .py file, the file is a module that can be imported just like any other. 

# You can then import these files into scripts:
import myCats
print(myCats.cats)
#[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
print(myCats.cats[0])
#{'desc': 'chubby', 'name': 'Zophie'}
print(myCats.cats[1])
#{'desc': 'fluffy', 'name': 'Pooka'}

#The benefit of creating a .py file (as opposed to saving variables with
#the shelve module) is that because it is a text file, the contents of the file
#can be read and modified by anyone with a simple text editor. For most
#applications, however, saving data using the shelve module is the preferred
#way to save variables to a file. Only basic data types such as integers, floats,
#strings, lists, and dictionaries can be written to a file as simple text. File
#objects, for example, cannot be encoded as text.
