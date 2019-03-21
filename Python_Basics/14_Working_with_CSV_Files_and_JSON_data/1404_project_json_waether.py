#! python3
#1404_project_json_waether.py - Project: Fetching Current Weather Data

#Checking the weather seems fairly trivial: Open your web browser, click the
#address bar, type the URL to a weather website (or search for one and then
#click the link), wait for the page to load, look past all the ads, and so on.
#Actually, there are a lot of boring steps you could skip if you had a program 
#that downloaded the weather forecast for the next few days and printed it as 
#plaintext. This program uses the requests module from Chapter 11 to download 
#data from the Web.

#Overall, the program does the following:
#•	 Reads the requested location from the command line.
#•	 Downloads JSON weather data from OpenWeatherMap.org.
#•	 Converts the string of JSON data to a Python data structure.
#•	 Prints the weather for today and the next two days.

#So the code will need to do the following:
#•	 Join strings in sys.argv to get the location.
#•	 Call requests.get() to download the weather data.
#•	 Call json.loads() to convert the JSON data to a Python data structure.
#•	 Print the weather forecast.

#####################################################
#Step 1: Get Location from the Command Line Argument#
#####################################################

import json, requests, sys, pprint

# Compute location from command line arguments.
if len(sys.argv) < 2:
	print('Usage: 1404_project_json_waether.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])
print(location)
#Command line arguments are split on spaces. The command line argument San Francisco, CA would make sys.argv hold ['quickWeather.py', 'San',
#'Francisco,', 'CA']. Therefore, call the join() method to join all the strings except for the first in sys.argv. 

################################
#Step 2: Download the JSON Data#
################################
#OpenWeatherMap.org provides real-time weather information in
#JSON format. Your program simply has to download the page at
#http://api.openweathermap.org/data/2.5/forecast/daily?q=<Location>&cnt=3,
#where <Location> is the name of the city whose weather you want.

#Warning - API needs subsription, so we use a test api call instead
#https://samples.openweathermap.org/data/2.5/forecast?q=London,us&appid=b6907d289e10d714a6e88b30761fae22
###################
#url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3'.format(str(location))
#response = requests.get(url)
#response.raise_for_status()
###################

url = 'https://samples.openweathermap.org/data/2.5/forecast?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
response = requests.get(url)
response.raise_for_status()

#Step 3: Load JSON Data and Print Weather
weatherData = json.loads(response.text)
#pprint.pprint(weatherData)
w = weatherData['list']
print('Current weather in %s:' % (location))
for i in range(0, len(w)):
	print('Today + {}'.format(str(i)))
	print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])

input("Press enter to exit ;)")

#Ideas for Similar Programs
#Accessing weather data can form the basis for many types of programs. You
#can create similar programs to do the following:
#•	 Collect weather forecasts for several campsites or hiking trails to see
#		which one will have the best weather.
#•	 Schedule a program to regularly check the weather and send you a frost
#		alert if you need to move your plants indoors. (Chapter 15 covers scheduling, and Chapter 16 explains how to send email.)
#•	 Pull weather data from multiple sites to show all at once, or calculate
#		and show the average of the multiple weather predictions.
