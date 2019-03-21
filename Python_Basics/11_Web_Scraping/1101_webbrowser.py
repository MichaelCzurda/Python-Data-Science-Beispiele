#!python3
#1101_webbrowser.py - Project: mapIt.py with the webbrowser Module

#In this chapter, you will learn about several modules that
#make it easy to scrape web pages in Python

#webbrowser		-	 Comes with Python and opens a browser to a specific page.
#Requests		-	 Downloads files and web pages from the Internet.
#Beautiful Soup	-	 Parses HTML, the format that web pages are written in.
#Selenium 		-	 Launches and controls a web browser. Selenium is able to
#					 fill in forms and simulate mouse clicks in this browser.

import webbrowser, sys, pyperclip
#open website
#webbrowser.open('http://inventwithpython.com/')

#A web browser tab will open to the URL http://inventwithpython.com/ - the only thing the webbrowser module can do
#Even so, the open() function does make some interesting things possible. For example,
#it’s tedious to copy a street address to the clipboard and bring up a map of
#it on Google Maps. You could take a few steps out of this task by writing a
#simple script to automatically launch the map in your browser using the
#contents of your clipboard. This way, you only have to copy the address to a
#clipboard and run the script, and the map will be loaded for you.

#This is what your program does:
#•	 Gets a street address from the command line arguments or clipboard.
#•	 Opens the web browser to the Google Maps page for the address.

#This means your code will need to do the following:
#•	 Read the command line arguments from sys.argv.
#•	 Read the clipboard contents.
#•	 Call the webbrowser.open() function to open the web browser.

#############################################################
#Step 1 Figure out the URL				  					#
#Step 2: Handle the Command Line Arguments					#
#Step 3: Handle the Clipboard Content and Launch the Browser#
#############################################################

#Example call: C:\> mapit 870 Valencia St, San Francisco, CA 94110
# the script will use the command line arguments instead of the clipboard. If there are no command line arguments, 
#then the program will know to use the contents of the clipboard.

#Step 1
if len(sys.argv) > 1:
	#Step 2
	#Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	#Step3
	address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

#Ideas for Similar Programs:
#•	 Open all links on a page in separate browser tabs.
#•	 Open the browser to the URL for your local weather.
#•	 Open several social network sites that you regularly check.
