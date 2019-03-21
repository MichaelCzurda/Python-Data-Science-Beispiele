#!python3
#0901_shutil_module.py - The shutil Module

#Your programs can also organize preexisting files on the hard drive. Maybe you’ve had the
#experience of going through a folder full of dozens, hundreds, or even thousands of files and copying,
#renaming, moving, or compressing them all by hand. 

#Possible tasks:
#	copy all pdfs in every subfolders
#	removing leading zeros in filenames
#	Compressing content of several folders into one ZIP


#THE SHUTIL MODULE
# functions to let you copy, move, rename, and delete files in your Python programs.

import shutil, os

###########################
#Copying Files and Folders#
###########################
#Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination.
# If destination is a filename, it will be used as the new name of the copied file. 
# return value is the path of the copied file

os.chdir('C:\\')
#same name 
print(shutil.copy('C:\\windows-version.txt', 'C:\\Users\\michaelc.AITC\\Documents\\Python Scripts\\ATBS\\09_Organizing_Files'))
#C:\Users\michaelc.AITC\Documents\Python Scripts\ATBS\09_Organizing_Files\windows-version.txt

#new name
print(shutil.copy('C:\\windows-version.txt', 'C:\\Users\\michaelc.AITC\\Documents\\Python Scripts\\ATBS\\09_Organizing_Files\\test.txt'))
#C:\Users\michaelc.AITC\Documents\Python Scripts\ATBS\09_Organizing_Files\test.txt

# shutil.copytree() willcopy an entire folder and every folder and file contained in it. 
#Calling shutil.copytree(source, destination) will copy the folder at the path
#source, along with all of its files and subfolders, to the folder at the path destination. 

#######################################
#Moving and Renaming Files and Folders#
#######################################
#Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return 
#a string of the absolute path of the new location.

#Example:
#shutil.move('C:\\bacon.txt', 'C:\\eggs')

#if Folder allready exists -> move into folder(existing files will be overwritten)

#The destination path can also specify a filename. In the following example, the source file is moved and renamed.
#shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')

#Both of the previous examples worked under the assumption that there
#was a folder eggs in the C:\ directory. But if there is no eggs folder, then move()
#will rename bacon.txt to a file named eggs.
#This can be a tough-to-spot bug in your programs since the move() call can happily do something that might be
#quite different from what you were expecting. 

########################################
#Permanently Deleting Files and Folders#
########################################
#You can delete a single file or a single empty folder with functions in the os module, 
#whereas to delete a folder and all of its contents, you use the shutil module.
#•	 Calling os.unlink(path) will delete the file at path.
#•	 Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
#•	 Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

#Good idea -> run program with these calls commented out and print() calls added to show the files that would be deleted
for filename in os.listdir():
	if filename.endswith('.rxt'):
		#os.unlink(filename)
		print(filename)

#########################################
#Safe Deletes with the send2trash Module#
#########################################
#Since Python’s built-in shutil.rmtree() function irreversibly deletes files and folders, it can be dangerous to use
#better solution -> send2trash
#send files/folders to Computers trash
#able to restore
import send2trash
send2trash.send2trash("C:\\Users\\michaelc.AITC\\Documents\\Python Scripts\\ATBS\\09_Organizing_Files\\test.txt")

#But while sending files to the recycle bin lets you
#recover them later, it will not free up disk space like permanently deleting
#them does. If you want your program to free up disk space, use the os and
#shutil functions for deleting files and folders. 
