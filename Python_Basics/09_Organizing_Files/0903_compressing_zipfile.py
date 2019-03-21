#!python3
#0903_compressing_zipfile.py - Compressing Files with the zipfile Module

#Your Python programs can both create and open (or extract) ZIP files using functions in the zipfile module. 
#Example zip -> example.zip

###################
#Reading ZIP Files#
###################

import zipfile, os

#First create ZipFile object
exampleZip = zipfile.ZipFile('example.zip')

#namelist() method that returns a list of strings for all the files and folders contained in the ZIP file
print(exampleZip.namelist())
#['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']

#getinfo() ZipFile method to return a ZipInfo object about that particular file
spamInfo = exampleZip.getinfo('spam.txt')
#FileSize
print(spamInfo.file_size)
#13908
print(spamInfo.compress_size)
#3828
print('Compressed file is {}x smaller!'.format(round(spamInfo.file_size / spamInfo.compress_size, 2)))
#Compressed file is 3.63x smaller!
exampleZip.close()

###########################
#Extracting from ZIP Files#
###########################
# extractall() method for ZipFile objects extracts all the files and folders from a ZIP file into the current working directory.
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

#Optionally, you can pass a folder name to extractall() to have it extract the files into a folder other than the current working directory. 
#not exists -> created

#The extract() method for ZipFile objects will extract a single file from the ZIP file.
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extract('spam.txt')
exampleZip.close()
#The string you pass to extract() must match one of the strings in the list returned by namelist()

##################################
#Creating and Adding to ZIP Files#
##################################
#To create your own compressed ZIP files, you must open the ZipFile object in write mode by passing 'w' as the second argument. 
#When you pass a path to the write() method of a ZipFile object, Python will compress the file at that path and add it into the ZIP file. The write()
#method’s first argument is a string of the filename to add. The second argument is the compression type parameter, which tells the computer what 
#algorithm it should use to compress the files; you can always just set this value to zipfile.ZIP_DEFLATED.

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

#Keep in mind that, just as with writing to files, write mode will erase all existing contents of a ZIP file. If you want to simply 
#add files to an existing ZIP file, pass 'a' as the second argument to zipfile.ZipFile() to open the ZIP file in append mode.
