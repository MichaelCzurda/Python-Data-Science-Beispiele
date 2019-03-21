#! python3
#1501_time_module.py - The time Module

#Your computer’s system clock is set to a specific date, time, and time zone.
#The built-in time module allows your Python programs to read the system
#clock for the current time. The time.time() and time.sleep() functions are
#the most useful in the time module.

##########################
#The time.time() Function#
##########################

#The Unix epoch is a time reference commonly used in programming: 12 am
#on January 1, 1970, Coordinated Universal Time (UTC). The time.time()
#function returns the number of seconds since that moment as a float value.
# This number is called an epoch timestamp. 

import time
print(time.time())
#1553005464.910835

#The return value is how many seconds have passed between the Unix epoch and the moment time.time() was called.
#Epoch timestamps can be used to profile code, that is, measure how long a piece of code takes to run.
#Measuring at beginning of the code, at the end , subtract:

def calcProd():
	# Calculate the product of the first 100,000 numbers.
	product = 1
	for i in range(1, 100000):
		product *= i
	return product
	
startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is {} digits long.'.format(str(len(str(prod)))))
print('Took {} seconds to calculate.'.format(str(endTime - startTime)))

#Another way to profile your code is to use the cProfile.run() function, which provides
#a much more informative level of detail than the simple time.time() technique. The
#cProfile.run() function is explained at https://docs.python.org/3/library/
#profile.html. 

###########################
#The time.sleep() Function#
###########################
#If you need to pause your program for a while, call the time.sleep() function
#and pass it the number of seconds you want your program to stay paused. 

for i in range(3):
	print('Tick')
	time.sleep(1)
	print('Tock')
	time.sleep(1)

#Be aware that pressing ctrl-C will not interrupt time.sleep() calls
#in IDLE. IDLE waits until the entire pause is over before raising the
#KeyboardInterrupt exception. To work around this problem, instead of 
#having a single time.sleep(30) call to pause for 30 seconds, use a for loop to
#make 30 calls to time.sleep(1).

##################
#Rounding numbers#
##################
#When working with times, you’ll often encounter float values with many
#digits after the decimal. To make these values easier to work with, you can
#shorten them with Python’s built-in round() function

now = time.time()
print(now)
print(round(now,2))
print(round(now,4))
print(round(now))
