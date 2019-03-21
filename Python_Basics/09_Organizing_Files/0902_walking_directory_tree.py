#!python3
#0902_walking_directory_tree.py - The shutil Module

#Say you want to rename every file in some folder and also every file in every
#subfolder of that folder. That is, you want to walk through the directory tree,
#touching each file as you go. Writing a program to do this could get tricky;
#fortunately, Python provides a function to handle this process for you.

#Example of os.walk

import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\michaelc.AITC\\Documents\\Python Scripts\\ATBS'):
	print('The current folder is ' + folderName)
	
	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' +subfolder)
		
	for filename in filenames:
		print('FILE INSIDE '+ folderName + ': ' + filename)
#output see in file walk_output.txt

#The os.walk() function is passed a single string value: the path of a
#folder. You can use os.walk() in a for loop statement to walk a directory
#tree, much like how you can use the range() function to walk over a range of
#numbers. Unlike range(), the os.walk() function will return three values on
#each iteration through the loop:
#1. A string of the current folder’s name (folder for current iteration of the for loop)
#2. A list of strings of the folders in the current folder
#3. A list of strings of the files in the current folder

#Since os.walk() returns lists of strings for the subfolder and filename
#variables, you can use these lists in their own for loops. Replace the print()
#function calls with your own custom code. (
