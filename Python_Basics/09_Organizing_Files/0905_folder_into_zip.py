#!python3
#0905_folder_into_zip.py - Project: Backing Up a Folder into a ZIP File

#create ZIP file “snapshots” from an entire folder. You’d like to keep different versions, so you want the ZIP file’s filename to increment each
#time it is made; for example, {name}_1.zip, {name}_2.zip, {name}_3.zip, and so on. 
#Write a program that does this task for you.

#The code for this program will be placed into a function named backupToZip().
#This will make it easy to copy and paste the function into other Python programs that need this functionality. 

##########################################################
#Step 1: Figure Out the ZIP File’s Name					 #
#Step 2: Create the New ZIP File	 					 #
#Step 3: Walk the Directory Tree and Add to the ZIP File #
##########################################################

import zipfile, os

def backupToZip(folder):

#Step 1	
	folder = os.path.abspath(folder) #make sure folder is absolute
	
	# Figure out the filename this code should use based on what files already exist.
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		print(zipFilename)
		if not os.path.exists(os.path.join(folder,zipFilename)):
			break
		number +=1

#Step 2	
	print('Creating {}....format(zipFilename)')
	backupZip = zipfile.ZipFile(os.path.join(folder,zipFilename), 'w')

#Step 3
	for folderName, subfolders, filenames in os.walk(folder):
		print('Adding files in {}... '.format(folderName))
		# Add the current folder to the ZIP file.
		backupZip.write(folderName)
	
		# Add all the files in this folder to the ZIP file.
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue
			else:
				backupZip.write(os.path.join(folderName, filename))
				print(os.path.join(folderName, filename))
		
		
	backupZip.close()
 
	print('Done.')
backupToZip('C:\\Users\\michaelc.AITC\\Documents\\Python Scripts\\ATBS')
