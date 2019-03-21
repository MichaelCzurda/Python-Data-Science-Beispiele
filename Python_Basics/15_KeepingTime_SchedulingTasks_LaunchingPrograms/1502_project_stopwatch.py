#! python3
#1502_project_stopwatch.py - Project: Super Stopwatch

#Say you want to track how much time you spend on boring tasks you haven’t
#automated yet. You don’t have a physical stopwatch, and it’s surprisingly 
#difficult to find a free stopwatch app for your laptop or smartphone that isn’t
#covered in ads and doesn’t send a copy of your browser history to marketers. 

#You can write a simple stopwatch program yourself in Python. 

#At a high level, here’s what your program will do:
#•	 Track the amount of time elapsed between presses of the enter key,
#		with each key press starting a new “lap” on the timer.
#•	 Print the lap number, total time, and lap time.

#This means your code will need to do the following:
#•	 Find the current time by calling time.time() and store it as a timestamp
#		at the start of the program, as well as at the start of each lap.
#•	 Keep a lap counter and increment it every time the user presses enter.
#•	 Calculate the elapsed time by subtracting timestamps.
#•	 Handle the KeyboardInterrupt exception so the user can press ctrl-C to quit.

###########################################
#Step 1: Set Up the Program to Track Times#
###########################################

import time

#Display instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

###################################
#Step 2: Track and Print Lap Times#
###################################
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# Handle the Ctrl-C exception to keep its error message from displaying.
	print('\nDone.')

#If the user presses ctrl-C to stop the stopwatch, the KeyboardInterrupt
#exception will be raised, and the program will crash if its execution is not
#a try statement. To prevent crashing, we wrap this part of the program in a
#try statement. We’ll handle the exception in the except clause , so when
#ctrl-C is pressed and the exception is raised, the program execution moves
#to the except clause to print Done, instead of the KeyboardInterrupt error message.

#Ideas for Similar Programs
#•	 Create a simple timesheet app that records when you type a person’s
#		name and uses the current time to clock them in or out.
#•	 Add a feature to your program to display the elapsed time since a
#		process started, such as a download that uses the requests module.
#•	 Intermittently check how long a program has been running and offer
#		the user a chance to cancel tasks that are taking too long.
