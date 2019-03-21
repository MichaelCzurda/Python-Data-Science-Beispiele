#! python3
#1505_multithreading.py - Multithreading

#To introduce the concept of multithreading, let’s look at an example situation. 
#Say you want to schedule some code to run after a delay or at a specific time.
#You could add code like the following at the start of your program:

#import time, datetime
#starttime = datetime.datetime(2029,10,31,0,0,0)
#while datetime.datetime.now() < startTime:
#	time.sleep(1)
#print('Program now starting on Halloween 2029')

# Your program cannot do anything while waiting for the loop of time.sleep() calls to finish; 
#it just sits around until Halloween 2029. This is because Python programs by default have a
#single thread of execution.

# a multithreaded program has multiple fingers. Each finger still moves to the next line of code as defined by
#the flow control statements, but the fingers can be at different places in the
#program, executing different lines of code at the same time. 

#Rather than having all of your code wait until the time.sleep() function finishes, 
#you can execute the delayed or scheduled code in a separate thread using Python’s 
#threading module. The separate thread will pause for the time.sleep calls. Meanwhile, 
#your program can do other work in the original thread. To make a separate thread, you 
#first need to make a Thread object by calling the threading.Thread() function.

import threading, time
print('Start of the program.')

def takeANap():
	time.sleep(3)
	print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program') 
#Start of the program.
#End of program
#Wake up!

#We define a function that we want to use in a new thread. To create a Thread object, we call threading.Thread() 
#and pass it the keyword argument target=takeANap. This means the function we want to call in the new thread 
#is takeANap(). Notice that the keyword argument is target=takeANap, not target=takeANap(). This is because you 
#want to pass the takeANap() function itself as the argument, not call takeANap() and pass its return value.
#After we store the Thread object created by threading.Thread() in threadObj, we call threadObj.start()  to 
#create the new thread and start executing the target function in the new thread. 

#A Python program will not terminate until all its threads have terminated. When you ran 1505_multithreading.py, 
#even though the original thread had terminated, the second thread was still executing the time.sleep(3) call.

###################################################
#Passing Arguments to the Thread’s Target Function#
###################################################

#If the target function you want to run in the new thread takes arguments, you can pass the target function’s 
#arguments to threading.Thread(). For example, say you wanted to run this print() call in its own thread:

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs','Frogs'], kwargs={'sep':' & '})
threadObj.start()
#Cats & Dogs & Frogs

#To make sure the arguments 'Cats', 'Dogs', and 'Frogs' get passed
#to print() in the new thread, we pass args=['Cats', 'Dogs', 'Frogs'] to
#threading.Thread(). 

#To make sure the keyword argument sep=' & ' gets
#passed to print() in the new thread, we pass kwargs={'sep': '& '} to
#threading.Thread().

#WARNING
#threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
#Example above is wrong:
#What this ends up doing is calling the print() function and passing its
#return value (print()’s return value is always None) as the target keyword
#argument. It doesn’t pass the print() function itself. When passing arguments 
#to a function in a new thread, use the threading.Thread() function’s
#args and kwargs keyword arguments.

####################
#Concurrency Issues#
####################

#You can easily create several new threads and have them all running at the
#same time. But multiple threads can also cause problems called concurrency
#issues. These issues happen when threads read and write variables at the
#same time, causing the threads to trip over each other. Concurrency issues
#can be hard to reproduce consistently, making them hard to debug.
#Multithreaded programming is its own wide subject and beyond the
#scope of this book. What you have to keep in mind is this: To avoid concurrency issues, 
#never let multiple threads read or write the same variables.
#When you create a new Thread object, make sure its target function uses only
#local variables in that function. This will avoid hard-to-debug concurrency
#issues in your programs.

#A beginner’s tutorial on multithreaded programming is available at http://nostarch.com/automatestuff/.

