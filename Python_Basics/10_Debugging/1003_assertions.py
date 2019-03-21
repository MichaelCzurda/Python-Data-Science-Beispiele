#!python3
#1003_assertions.py - Assertions

#An assertion is a sanity check to make sure your code isn’t doing something
#obviously wrong. These sanity checks are performed by assert statements. If
#the sanity check fails, then an AssertionError exception is raised. In code, an
#assert statement consists of the following:
#•	 The assert keyword
#•	 A condition (that is, an expression that evaluates to True or False)
#•	 A comma
#•	 A string to display when the condition is False

#Example:
#podBayDoorStatus = 'open'
#assert podBayDoorStatus == 'open',  'The pod bay doors need to be "open".'
#podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
#assert podBayDoorStatus == 'open',  'The pod bay doors need to be "open".'
#Traceback (most recent call last):
#  File "1003_assertions.py", line 17, in <module>
#    assert podBayDoorStatus == 'open',  'The pod bay doors need to be "open".'
#AssertionError: The pod bay doors need to be "open".

#Unlike exceptions, your code should not handle assert statements with try and
#except; if an assert fails, your program should crash. By failing fast like this,
#you shorten the time between the original cause of the bug and when you
#first notice the bug. This will reduce the amount of code you will have to
#check before finding the code that’s causing the bug.

#Assertions are for programmer errors, not user errors. For errors that can be recovered from 
#(such as a file not being found or the user entering invalid data), 
#raise an exception instead of detecting it with an assert statement.

##################################################
#Using an Assertion in a Traffic Light Simulation#
##################################################
#The data structure representing the stoplights at an intersection is a dictionary with 
#keys 'ns' and 'ew', for the stoplights facing north-south and east-west,
#respectively. The values at these keys will be one of the strings 'green',
#'yellow', or 'red'. The code would look something like this:
market_2nd = {'ns':'green', 'ew':'red'}
mission_16th = {'ns':'red', 'ew':'green'}

# switchLights() function, which will take an intersection dictionary as an argument and switch the lights.
def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key]='yellow'
		elif stoplight[key]=='yellow':
			stoplight[key]='red'
		elif stoplight[key]=='red':
			stoplight[key]='green'
	assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)		
switchLights(market_2nd)
#With this assertion in place, your program would crash if no direction is red

######################
#Diasbling Assertions#
######################
#Assertions can be disabled by passing the -O option when running Python.
#This is good for when you have finished writing and testing your program
#and don’t want it to be slowed down by performing sanity checks 
#Assertions are for development, not the final product. 

#You can disable the assert statements in your Python programs for a slight
#performance improvement. When running Python from the terminal,
#include the -O switch after python or python3 and before the name of the
#.py file. This will run an optimized version of your program that skips the
#assertion checks.
