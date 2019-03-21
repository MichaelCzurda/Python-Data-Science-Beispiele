#! python3
#0802_os_path_module.py - The os.path Module

#os.path module contains many useful functions
#Example -> os.path.join

######################################
#HANDLING ABSOLUTE AND RELATIVE PATHS#
######################################

#os.path.abspath(path) -> return string of absolute path
#os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path
#os.path.relpath(path, start) will return a string of a relative path from the start path to path.

import os
print(os.path.abspath('.'))
#C:\Users\michaelc.AITC\Documents\Python Scripts\ATBS\08_Reading_and_Writing_Files
print(os.path.isabs('.'))
#False
print(os.path.isabs(os.path.abspath('.')))
#True

print(os.path.relpath('C:\\Windows', 'C:\\'))
#Windows
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
#..\..\Windows

#The base name follows the last slash in a path and is the same as the filename. The dir
#name is everything before the last slash
#Example
path='C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
#calc.exe
print(os.path.dirname(path))
#C:\Windows\System32

#If you need a path’s dir name and base name together, you can just call
#os.path.split() to get a tuple value with these two strings, like so:
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(path))
#('C:\\Windows\\System32', 'calc.exe')

#note that os.path.split() does not take a file path and return a list
#of strings of each folder. For that, use the split() string method and split on
#the string in os.sep. 
print(calcFilePath.split(os.sep))
#['C:', 'Windows', 'System32', 'calc.exe']

########################################
#FINDING FILE SIZES AND FOLDER CONTENTS#
########################################
# The os.path module provides functions for finding the size of a file in bytes and the 
#files and folders inside a given folder.

#os.path.getsize(path) will return the size in bytes of the file in the path argument.
#os.listdir(path) will return a list of filename strings for each file in the path argument. 

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
#933888 Bytes
print(os.listdir('C:\\Windows\\System32'))
#List.....

#If I want to find the total size of all the files in this directory, I can use os.path.getsize() and
#os.listdir() together:

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
	totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
#2066421164 Bytes

########################
#CHECKING PATH VALIDITY#
########################
#Many Python functions will crash with an error if you supply them with a path that does not exist. 
#os.path module provides functions to check whether a given path exists and whether it is a file or folder.

#os.path.exists(path) will return True if the file or folder referred to in the argument exists otherwise False
#os.path.isfile(path) will return True if the path argument exists and is a file and will return False otherwise.
#os.path.isdir(path) will return True if the path argument existsn and is a folder and will return False otherwise.
