#!python3
#1102_downloading_files_with_request.py - Downloading Files from the Web with the requests Module

#The requests module lets you easily download files from the Web without having to worry about 
#complicated issues such as network errors, connection problems,  and data compression. 
#The requests module doesn’t come with Python, so you’ll have to install it first. 


#########################################################
#Downloading a Web Page with the requests.get() Function#
#########################################################

#The requests.get() function takes a string of a URL to download. By calling
#type() on requests.get()’s return value, you can see that it returns a Response
#object, which contains the response that the web server gave for your request. 

#Example:
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
#<class 'requests.models.Response'>
print(res.status_code == requests.codes.ok)
#True

#If the request succeeded, the downloaded web page is stored as a string in the Response object’s text variable. 
print(len(res.text))
#178978
print(res.text[:250])
#The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare
#This eBook is for the use of anyone anywhere at no cost and with
#almost no restrictions whatsoever.  You may copy it, give it away or
#re-use it under the terms of the Projec


#####################
#Checking for Errors#
#####################

#Response object has a status_code to see whether the download succeded
#A simpler way -> call the raise_for_status() method on the Response object
#raise exception if there was an error

#res = requests.get('https://automatetheboringstuff.com/_page_does_not_exists')
#res.raise_for_status()

#The raise_for_status() method is a good way to ensure that a program
#halts if a bad download occurs

#If a failed download isn’t a deal breaker for your program, you can wrap the 
#raise_for_status() line with try and except statements to handle this error case without crashing

res = requests.get('https://automatetheboringstuff.com/_page_does_not_exists')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: {}'.format(exc))
	
#Always call raise_for_status() after calling requests.get(). You want to be
#sure that the download has actually worked before your program continues.

###########################################
#Saving Downloaded Files to the Hard Drive#
###########################################
#save webpage with open() and write()
#Differences -> must write file in write binary by passing string 'wb' as the second argument to open() => to remain unicode encoding
#write page to file with a for loop and the Response objects#s iter_content() method:

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile= open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)
playFile.close()

#iter_content() method returns chunks of the content on each iteration. each chunk is of bytes data type -> specify how many bytes each chunk will contain, 100000 generally good
#Review:
#1. Call requests.get() to download the file.
#2. Call open() with 'wb' to create a new file in write binary mode.
#3. Loop over the Response object’s iter_content() method.
#4. Call write() on each iteration to write the content to the file.
#5. Call close() to close the file.

#Docu requests:  http://requests.readthedocs.org/
