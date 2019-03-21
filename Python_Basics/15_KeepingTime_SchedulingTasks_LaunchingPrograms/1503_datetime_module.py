#! python3
#1503_datetime_module.py - The datetime Module

#The time module is useful for getting a Unix epoch timestamp to work with.
#But if you want to display a date in a more convenient format, or do arithmetic 
#with dates (for example, figuring out what date was 205 days ago or
#what date is 123 days from now), you should use the datetime module.
#The datetime module has its own datetime data type. datetime values
#represent a specific moment in time.


import datetime, time

#Calling datetime.datetime.now() u returns a datetime object v for the
#current date and time, according to your computer’s clock.
print(datetime.datetime.now())
#2019-03-19 16:04:36.184618

#You can also retrieve a datetime object for a specific
#moment by using the datetime.datetime() function w, passing it integers 
#representing the year, month, day, hour, and second of the moment you want. 
dt = datetime.datetime(2015,10,21,16,29,0)
print((dt.year, dt.month, dt.day))
#(2015, 10, 21)
print((dt.hour, dt.minute, dt.second))
#(16, 29, 0)

#A Unix epoch timestamp can be converted to a datetime object with the
#datetime.datetime.fromtimestamp() function. The date and time of the datetime
#object will be converted for the local time zone. 

print(datetime.datetime.fromtimestamp(1000000))
#1970-01-12 14:46:40
print(datetime.datetime.fromtimestamp(time.time()))
#2019-03-19 16:09:41.204616

# So the expressions datetime.datetime.now() and datetime.datetime.fromtimestamp(time.time()) do the same thing

#datetime objects can be compared with each other using comparison
#operators to find out which one precedes the other. The later datetime
#object is the “greater” value. 
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(halloween2015 == oct31_2015)
#True
print(halloween2015 > newyears2016)
#False
print(newyears2016 > halloween2015)
#True
print(newyears2016 != oct31_2015)
#True

#########################
#The timedelta Data Type#
#########################
#The datetime module also provides a timedelta data type, which represents a
#duration of time rather than a moment in time.
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(( delta.days, delta.seconds, delta.microseconds))
#(11, 36548, 0)
# This timedelta object’s days attributes stores 11, and its seconds attribute stores 36548 (10 hours, 9 minutes, and 8 seconds, expressed in seconds) 
print(delta.total_seconds())
#986948.0
print(str(delta))
#11 days, 10:09:08

#The datetime.timedelta() function takes keyword arguments weeks, days, hours,
#minutes, seconds, milliseconds, and microseconds.

#There is no month or year keyword argument because “a month” or “a year” is a variable amount of time
#depending on the particular month or year. A timedelta object has the total
#duration represented in days, seconds, and microseconds. 
#These numbers are stored in the days, seconds, and microseconds attributes, respectively
# The total_seconds() method will return the duration in number of seconds
#alone. Passing a timedelta object to str() will return a nicely formatted,
#human-readable string representation of the object. 

#The arithmetic operators can be used to perform date arithmetic on datetime values.
# For example, to calculate the date 1,000 days from now
dt = datetime.datetime.now()
print(dt)
#2019-03-19 16:33:40.165904
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)
#2021-12-13 16:33:40.165904

#timedelta objects can be added or subtracted with datetime objects or
#other timedelta objects using the + and - operators. A timedelta object can be
#multiplied or divided by integer or float values with the * and / operators. 
oct21st = datetime.datetime(2015,10,21,16,29,0)
aboutThirtyYears=datetime.timedelta(days = 365 * 30)
print(oct21st)
#2015-10-21 16:29:00
print( oct21st - aboutThirtyYears)
#1985-10-28 16:29:00
print( oct21st + aboutThirtyYears)
#2045-10-13 16:29:00
print(oct21st - (2 * aboutThirtyYears))
#1955-11-05 16:29:00

###############################
#Pausing Until a Specific Date#
###############################
#The time.sleep() method lets you pause a program for a certain number of seconds. 
#By using a while loop, you can pause your programs until a specific date.
#For example, the following code will continue to loop until Halloween 2019:
halloween2019 = datetime.datetime(2019,10,31,0,0,0)
#while datetime.datetime.now() < halloween2019:
#	time.sleep(1)

##########################################
#Converting datetime Objects into Strings#
##########################################
#Epoch timestamps and datetime objects aren’t very friendly to the human
#eye. Use the strftime() method to display a datetime object as a string. (The
#f in the name of the strftime() function stands for format.)
#The strftime() method uses directives similar to Python’s string formatting. 

#strftime() Directives:

#strftime 	directive Meaning

#%Y 		Year with century, as in '2014'
#%y 		Year without century, '00' to '99' (1970 to 2069)
#%m 		Month as a decimal number, '01' to '12'
#%B 		Full month name, as in 'November'
#%b 		Abbreviated month name, as in 'Nov'
#%d 		Day of the month, '01' to '31'
#%j 		Day of the year, '001' to '366'
#%w 		Day of the week, '0' (Sunday) to '6' (Saturday)
#%A 		Full weekday name, as in 'Monday'
#%a 		Abbreviated weekday name, as in 'Mon'
#%H 		Hour (24-hour clock), '00' to '23'
#%I 		Hour (12-hour clock), '01' to '12'
#%M 		Minute, '00' to '59'
#%S 		Second, '00' to '59'
#%p 		'AM' or 'PM'
#%% 		Literal '%' character

#Pass strrftime() a custom format string containing formatting directives 
#(along with any desired slashes, colons, and so on), and strftime() will
#return the datetime object’s information as a formatted string.

oct21st = datetime.datetime(2019,10,21,16,29,0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
#2019/10/21 16:29:00
print(oct21st.strftime('%I:%M %p'))
#04:29 PM
print( oct21st.strftime("%B of '%y"))
#October of '19

##########################################
#Converting Strings into datetime Objects#
##########################################
#If you have a string of date information, such as '2015/10/21 16:29:00'
#or 'October 21, 2015', and need to convert it to a datetime object, use the
#datetime.datetime.strptime() function. The strptime() function is the inverse
#of the strftime() method.
print()
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
#2015-10-21 00:00:00
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
#2015-10-21 16:29:00
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
#2015-10-01 00:00:00
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
#2063-11-01 00:00:00

#The string with the date information must match the custom format string
#exactly, or Python will raise a ValueError exception.
