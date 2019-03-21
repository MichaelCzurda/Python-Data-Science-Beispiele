#! python3
#0801_files_and_paths.py - Files and File Paths

#root Directory
#Windows => C:\
#Linux and OSX => /

#Additional volums(usb, dvd)
#Windows => D:\ or E:\
#Linux => new Fodlers in /mnt 
#OSX => new Folder in /Volumes

#Backslash on Windows and Forward Slash on OS X and Linux
#Windows => Bachslash
#Linux nad OSX => Forward Slash
#Python Script to handle both cases:
#Fortunately, this is simple to do with the os.path.join() function. If you
#pass it the string values of individual file and folder names in your path,
#os.path.join() will return a string with a file path using the correct path
#separators.
import os
print(os.path.join('C:\\', 'bin','spam'))
#C:\bin\spam

#For example, the following example joins names from a list of filenames to the end of a folder’s name:
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('C:\\Users\\asweigart', filename))
#C:\Users\asweigart\accounts.txt
#C:\Users\asweigart\details.csv
#C:\Users\asweigart\invite.docx

###############################
#THE CURRENT WORKING DIRECTORY#
###############################
#get cwd
print(os.getcwd())
#C:\Users\michaelc.AITC\Documents\Python Scripts\ATBS\08_Reading_and_Writing_Files

#change cwd -> os.chdir('C:\\Windows\\System32')

############################
#ABSOLUTE VS RELATIVE PATHS#
############################

#Two types
# An absolute path, which always begins with the root folder
# A relative path, which is relative to the program’s current working directory

#There are also the dot (.) and dot-dot (..) folders. These are not real
#folders but special names that can be used in a path. A single period (“dot”)
#for a folder name is shorthand for “this directory.” Two periods (“dot-dot”)
#means “the parent folder.”

#########################################
#CREATING NEW FOLDERS WITH os.makedirs()#
#########################################

#os.makedirs('C:\\delicious\\walnut\\waffles')
#This will create not just the C:\delicious folder but also a walnut folder
#inside C:\delicious and a waffles folder inside C:\delicious\walnut. That is,
#os.makedirs() will create any necessary intermediate folders in order to
#ensure that the full path exists.
