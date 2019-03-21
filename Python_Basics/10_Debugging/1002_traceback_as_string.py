#!python3
#1002_traceback_as_string.py - Getting the Traceback as a String

#When Python encounters an error, it produces a treasure trove of error information called the traceback.
#Traceback includes:
#	-error message
#	-line number that caused the error
#	-sequence of functions that led to the error - call stack 

def spam():
	bacon()

def bacon():
	raise Exception('This is the error message')
	
#spam()
#Traceback (most recent call last):
#  File "1002_traceback_as_string.py", line 16, in <module>
#    spam()
#  File "1002_traceback_as_string.py", line 11, in spam
#    bacon()
#  File "1002_traceback_as_string.py", line 14, in bacon
#    raise Exception('This is the error message')
#Exception: This is the error message

#The traceback is displayed by Python whenever a raised exception goes unhandled. But you can also obtain it as a string by calling
#traceback.format_exc().
#This function is useful if you want the information from an exception’s traceback but also want an except statement to gracefully 
#handle the exception. You will need to import Python’s traceback module before calling this function

#For example, instead of crashing your program right when an exception occurs, you can write the traceback information to a log file and keep
#your program running. You can look at the log file later, when you’re ready to debug your program.

import traceback
try:
	raise Exception('This is the error message.')
except:
	errorFile = open('error_info.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written to error_info.txt.')
