#!python3
#1001_raising_exceptions.py - Raising Exceptions

#Python raises an exception whenever it tries to execute invalid code.
#handle Python’s exceptions with try and except statements so that your program can recover from exceptions that you anticipated. 
#But you can also raise your own exceptions in your code. 

#Exceptions are raised with a raise statement. In code, a raise statement consists of the following:
#•	 The raise keyword
#•	 A call to the Exception() function
#•	 A string with a helpful error message passed to the Exception() function
#Example:
#raise Exception('This is the error message')

#If there are no try and except statements covering the raise statement that raised the exception, 
#the program simply crashes and displays the exception’s error message.

#Often it’s the code that calls the function, not the fuction itself, that knows how to handle an expection. 
#So you will commonly see a raise statement inside a function and the try and except statements in the code calling the function.
#Example:
def boxPrint(symbol, width, heigth):
	if len(symbol) != 1:
		raise Exception('Symbol must be a single character string.')
	if width <= 2:
		raise Exception('Width must be greater than 2.')
	if heigth <= 2:
		raise Exception('Length must be greater than 2.')
		
	print(symbol*width)
	for i in range(heigth -2):
		print(symbol+(' ' * (width - 2)) + symbol)
	print(symbol*width)

for s, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		boxPrint(s,w,h)
	except Exception as err:
		print('An exception happend: ' + str(err))
