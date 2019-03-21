#! python3
#1507_launching_programs.py - Launching Other Programs from Python

#Your Python program can start other programs on your computer with the
#Popen() function in the built-in subprocess module.  If you have multiple 
#instances of an application open, each of those instances is a separate 
#process of the same program. 

#Every process can have multiple threads. Unlike threads, a process cannot 
#directly read and write another process’s variables. If you think of a
#multithreaded program as having multiple fingers following source code,
#then having multiple processes of the same program open is like having
#a friend with a separate copy of the program’s source code. You are both
#independently executing the same program.

#If you want to start an external program from your Python script, pass
#the program’s filename to subprocess.Popen(). (On Windows, right-click the
#application’s Start menu item and select Properties to view the application’s 
#filename

import subprocess
#subprocess.Popen("C:\Windows\system32\calc.exe")

#The return value is a Popen object, which has two useful methods: poll()
#and wait(). You can think of the poll() method as asking your friend if she’s 
#finished running the code you gave her. The poll() method will return None if
#the process is still running at the time poll() is called. If the program has
#terminated, it will return the process’s integer exit code. An exit code is used 
#to indicate whether the process terminated without errors (an exit code
#of 0) or whether an error caused the process to terminate (a nonzero exit
#code—generally 1, but it may vary depending on the program).
#The wait() method is like waiting for your friend to finish working on
#her code before you keep working on yours. The wait() method will block
#until the launched process has terminated. This is helpful if you want your
#program to pause until the user finishes with the other program. The
#return value of wait() is the process’s integer exit code.

# Note that the wait() call will block until you quit the launched calculator program.
#calcProc = subprocess.Popen("C:\Windows\system32\calc.exe")
#print(calcProc.poll() == None)
#True
#print(calcProc.wait())
#Waits until the program is closed. The returns 0

###########################################
#Passing Command Line Arguments to Popen()#
###########################################

#You can pass command line arguments to processes you create with Popen().
#To do so, you pass a list as the sole argument to Popen(). The first string in
#this list will be the executable filename of the program you want to launch;
#all the subsequent strings will be the command line arguments to pass to
#the program when it starts. In effect, this list will be the value of sys.argv
#for the launched program.

#Most applications with a graphical user interface (GUI) don’t use command line arguments 
#as extensively as command line–based or terminalbased programs do. But most GUI applications 
#will accept a single argument for a file that the applications will immediately open when they
#start. For example, if you’re using Windows, create a simple text file called
#C:\hello.txt (in the working directory) and then enter the following:

subprocess.Popen(['C:\\Program Files (x86)\\Notepad++\\notepad++.exe', 'hello.txt'])

###################################
#Task Scheduler, launchd, and cron#
###################################
#If you are computer savvy, you may know about Task Scheduler on Windows,
#launchd on OS X, or the cron scheduler on Linux. These well-documented 
#and reliable tools all allow you to schedule applications to launch at specific
#times. If you’d like to learn more about them, you can find links to tutorials
#at http://nostarch.com/automatestuff/

#Using your operating system’s built-in scheduler saves you from writing
#your own clock-checking code to schedule your programs. However, use
#the time.sleep() function if you just need your program to pause briefly. Or
#instead of using the operating system’s scheduler, your code can loop until
#a certain date and time, calling time.sleep(1) each time through the loop.

##############################
#Opening Websites with Python#
##############################
#The webbrowser.open() function can launch a web browser from your program to a specific website, rather than opening the browser application
#with subprocess.Popen(). See “Project: mapIt.py with the webbrowser Module”
#on page 234 for more details.

##############################
#Running Other Python Scripts#
##############################
#You can launch a Python script from Python just like any other application. You just have to pass the python.exe 
#executable to Popen() and the filename of the .py script you want to run as its argument. 

subprocess.Popen(['C:\\Users\\michaelc.AITC\\AppData\\Local\\Continuum\\Anaconda3\\python.exe','hello.py'])

#########################################
#Opening Files with Default Applications#
#########################################
#Double-clicking a .txt file on your computer will automatically launch the
#application associated with the .txt file extension. Your computer will have
#several of these file extension associations set up already. Python can also
#open files this way with Popen().

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()

subprocess.Popen(['start', 'hello.txt'], shell=True)

#Here we write Hello world! to a new hello.txt file. Then we call Popen(),
#passing it a list containing the program name (in this example, 'start' for
#Windows) and the filename. We also pass the shell=True keyword argument,
#which is needed only on Windows. The operating system knows all of the
#file associations and can figure out that it should launch, say, Notepad.exe to
#handle the hello.txt file

#The Unix Philosophy
#Programs well designed to be launched by other programs become more powerful than their code alone. 
#The Unix philosophy is a set of software design principles established by the programmers of the Unix operating system (on which
#the modern Linux and OS X are built). It says that it’s better to write small, limitedpurpose programs 
#that can interoperate, rather than large, feature-rich applications. The smaller programs are easier to understand, 
#and by being interoperable, they can be the building blocks of much more powerful applications.
#Smartphone apps follow this approach as well. If your restaurant app needs
#to display directions to a café, the developers didn’t reinvent the wheel by writing their own map code. 
#The restaurant app simply launches a map app while passing it the café’s address, just as your Python code would call a function
#and pass it arguments.
#
#The Python programs you’ve been writing in this book mostly fit the Unix
#philosophy, especially in one important way: They use command line arguments rather than input() function calls. If all the information your program
#needs can be supplied up front, it is preferable to have this information passed
#as command line arguments rather than waiting for the user to type it in. This
#way, the command line arguments can be entered by a human user or supplied
#by another program. This interoperable approach will make your programs
#reusable as part of another program.
#The sole exception is that you don’t want passwords passed as command
#line arguments, since the command line may record them as part of its command history feature. Instead, your program should call the input() function
#when it needs you to enter a password.
#You can read more about Unix philosophy at https://en.wikipedia.org/wiki/
#Unix_philosophy/.
