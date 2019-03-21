#!python3
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#logging.disable(logging.CRITICAL)
#1004_logging.py - Logging

# Logging is a great way to understand what’s happening in your
#program and in what order its happening. Python’s logging module makes
#it easy to create a record of custom messages that you write. These log 
#messages will describe when the program execution has reached the logging
#function call and list any variables you have specified at that point in time.
#On the other hand, a missing log message indicates a part of the code was
#skipped and never executed.

##########################
#Using the logging Module#
##########################

#To enable the logging module to display log messages on your screen as your
#program runs, copy the following to the top of your program (but under
#the #! python shebang line):
#import logging
#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
#- %(message)s')

#when Python logs an event, it creates a LogRecord object that holds information about that event.
#basicConfig lets you specify what details to display

#Example
#function to calculate factorial
#there is a bug in the code - logging helps to find bug
def factorial(n):
	logging.debug('Start of factorial(%s%%)' % (n))
	total = 1
	for i in range(n + 1):
		#solution:  for i in range(1, n + 1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
		logging.debug('End of factorial(%s%%)' % (n))
	return total

print(factorial(5))
logging.debug('End of program')
print()
#2019-03-07 16:36:20,370 - DEBUG- Start of factorial(5%)
#2019-03-07 16:36:20,370 - DEBUG- i is 0, total is 0
#2019-03-07 16:36:20,370 - DEBUG- End of factorial(5%)
#2019-03-07 16:36:20,370 - DEBUG- i is 1, total is 0
#2019-03-07 16:36:20,370 - DEBUG- End of factorial(5%)
#2019-03-07 16:36:20,371 - DEBUG- i is 2, total is 0
#2019-03-07 16:36:20,371 - DEBUG- End of factorial(5%)
#2019-03-07 16:36:20,371 - DEBUG- i is 3, total is 0
#2019-03-07 16:36:20,371 - DEBUG- End of factorial(5%)
#2019-03-07 16:36:20,371 - DEBUG- i is 4, total is 0
#2019-03-07 16:36:20,371 - DEBUG- End of factorial(5%)
#2019-03-07 16:36:20,371 - DEBUG- i is 5, total is 0
#2019-03-07 16:36:20,372 - DEBUG- End of factorial(5%)
#0
#2019-03-07 16:36:20,372 - DEBUG- End of program

##########################
#Don't Debug with print()#
##########################
#logging > print()
#when removing the logging with print statement you have to remove every single print statement
# With logging you can disable them later by adding a single logging.disable(logging.CRITICAL) call. 
#Unlike print(), the logging module makes it easy to switch between showing and hiding log messages.

################
#Logging Levels#
################
#Logging levels provide a way to categorize your log messages by importance. 
#Five Levels:
#DEBUG - logging.debug() - The lowest level. Used for small details.Usually you care about these messages only when diagnosing problems.
#INFO - logging.info() - Used to record information on general events in your program or confirm that things are working at their point in the program.
#WARNING - logging.warning() - Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
#ERROR - logging.error() - Used to record an error that caused the program to fail to do something.
#CRITICAL - logging.critical() - The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely

#Up to you to choose which oen to use:
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
#The benefit of logging levels is that you can change what priority of
#logging message you want to see. Passing logging.DEBUG to the basicConfig()
#function’s level keyword argument will show messages from all the logging
#levels (DEBUG being the lowest level). But after developing your program
#some more, you may be interested only in errors. In that case, you can set
#basicConfig()’s level argument to logging.ERROR. This will show only ERROR
#and CRITICAL messages and skip the DEBUG, INFO, and WARNING messages. 

###################
#Disabling Logging#
###################
#After you’ve debugged your program, you probably don’t want all these
#log messages cluttering the screen. The logging.disable() function disables
#these so that you don’t have to go into your program and remove all the logging calls by hand. 
#You simply pass logging.disable() a logging level, and it
#will suppress all log messages at that level or lower. So if you want to disable
#logging entirely, just add logging.disable(logging.CRITICAL) to your program. 

###################
#Logging to a file#
###################
#The logging.basicConfig() function takes a filename keyword argument, like so:
#import logging
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
#%(asctime)s - %(levelname)s - %(message)s')
