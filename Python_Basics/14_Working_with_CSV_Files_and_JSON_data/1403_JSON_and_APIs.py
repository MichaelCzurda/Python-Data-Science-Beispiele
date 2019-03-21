#! python3
#1403_JSON_and_APIs.py - JSON and APIs

#JavaScript Object Notation is a popular way to format data as a single
#human-readable string. JSON is the native way that JavaScript programs
#write their data structures and usually resembles what Python’s pprint()
#function would produce.

#Example:
#{"name": "Zophie", "isCat": true,
# "miceCaught": 0, "napsTaken": 37.5,
# "felineIQ": null}

#JSON is useful to know, because many websites offer JSON content as
#a way for programs to interact with the website. This is known as providing an application programming interface (API). 
#Accessing an API is the same  as accessing any other web page via a URL. The difference is that the data
#returned by an API is formatted (with JSON, for example) for machines; APIs aren’t easy for people to read.

# You’ll have to find documentation for what URLs your program
#needs to request in order to get the data you want, as well as the general
#format of the JSON data structures that are returned. This documentation should be 
#provided by whatever site is offering the API; if they have
#a “Developers” page, look for the documentation there.

#Using APIs, you could write programs that do the following:
#•	 Scrape raw data from websites. (Accessing APIs is often more convenient
#		than downloading web pages and parsing HTML with Beautiful Soup.)
#•	 Automatically download new posts from one of your social network
#		accounts and post them to another account. For example, you could
#		take your Tumblr posts and post them to Facebook.
#•	 Create a “movie encyclopedia” for your personal movie collection by
#		pulling data from IMDb, Rotten Tomatoes, and Wikipedia and putting
#		it into a single text file on your computer

#You can see some examples of JSON APIs in the resources at http://nostarch.com/automatestuff/

#################
#THE JSON MODULE#
#################
#Python’s json module handles all the details of translating between a string
#with JSON data and Python values for the json.loads() and json.dumps()
#functions. JSON can’t store every kind of Python value. It can contain values
#of only the following data types: strings, integers, floats, Booleans, lists,
#dictionaries, and NoneType. JSON cannot represent Python-specific objects,
#such as File objects, CSV Reader or Writer objects, Regex objects, or Selenium
#WebElement objects.

########################################
#Reading JSON with the loads() Function#
########################################
#To translate a string containing JSON data into a Python value, pass it to the json.loads() function. (loads => "load string")

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
#{'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}

#Note that JSON strings always use double quotes. It will return that data as a 
#Python dictionary. Python dictionaries are not ordered, so the key-value pairs may 
#appear in a different order when you print jsonDataAsPythonValue.

########################################
#Writing JSON with the dumps() Function#
########################################
#The json.dumps() function (which means “dump string,” not “dumps”) will
#translate a Python value into a string of JSON-formatted data. 

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
#{"isCat": true, "miceCaught": 0, "name": "Zophie", "felineIQ": null}

#The value can only be one of the following basic Python data types: dictionary, list, integer, float, string, Boolean, or None.
