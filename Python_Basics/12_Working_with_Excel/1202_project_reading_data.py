#!python3
#1202_project_reading_data.py - Project: Reading Data from a Spreadsheet

#Say you have a spreadsheet of data from the 2010 US Census and you
#have the boring task of going through its thousands of rows to count both
#the total population and the number of census tracts for each county. 
#Data -> censuspopdata.xlsx

#Even though Excel can calculate the sum of multiple selected cells,
#you’d still have to select the cells for each of the 3,000-plus counties. Even
#if it takes just a few seconds to calculate a county’s population by hand,
#this would take hours to do for the whole spreadsheet.
#In this project, you’ll write a script that can read from the census spreadsheet 
#file and calculate statistics for each county in a matter of seconds.

#This is what your program does:
#•	 Reads the data from the Excel spreadsheet.
#•	 Counts the number of census tracts in each county.
#•	 Counts the total population of each county.
#•	 Prints the results.

#This means your code will need to do the following:
#•	 Open and read the cells of an Excel document with the openpyxl module.
#•	 Calculate all the tract and population data and store it in a data structure.
#•	 Write the data structure to a text file with the .py extension using the pprint module.

#####################################
#Step 1: Read the Spreadsheet Data  #
#Step 2: Populate the Data Structure#
#Step 3: Write the Results to a File#
#####################################

#There is just one sheet in the censuspopdata.xlsx spreadsheet, named
#'Population by Census Tract', and each row holds the data for a single census tract. 
#The columns are the tract number (A), the state abbreviation (B),
#the county name (C), and the population of the tract (D).


#The data structure stored in countyData will be a dictionary with state abbreviations as its keys. 
#Each state abbreviation will map to another dictionary,
#whose keys are strings of the county names in that state. Each county name
#will in turn map to a dictionary with just two keys, 'tracts' and 'pop'. These
#keys map to the number of census tracts and population for the county. 
#Example query: countyData[state abbrev][county]['pop']
#Example query: countyData[state abbrev][county]['tracts']

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
#countyData will contain the populations and number of tracts you calculate for each county.
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
	# Each row in the spreadsheet has data for one census tract.
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value 
	
	#step2
	#Make sure hte key for this state exists. To make sure the state abbreviation key exists
	#in your data structure, you need to call the setdefault() method to set a
	#value if one does not already exist for state
	countyData.setdefault(state, {})
	
	#Just as the countyData dictionary needs a dictionary as the value for each
	#state abbreviation key, each of those dictionaries will need its own dictionary
	#as the value for each county key. And each of those dictionaries in turn
	#will need keys 'tracts' and 'pop' that start with the integer value 0. 
	countyData[state].setdefault(county, {'tracts':0, 'pop':0})
	#Since setdefault() will do nothing if the key already exists, you can call
	#it on every iteration of the for loop without a problem. 
	
	countyData[state][county]['tracts'] += 1
	countyData[state][county]['pop'] += int(pop)
	
#Step3
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')
#The pprint.pformat() function produces a string that itself is formatted as valid Python code. 
#By outputting it to a text file named census2010.py,
#you’ve generated a Python program from your Python program! This may
#seem complicated, but the advantage is that you can now import census2010.py
#just like any other Python module. 

#import census2010.py
import census2010
print(census2010.allData['AK']['Anchorage'])
#{'pop': 291826, 'tracts': 55}
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))
#The 2010 population of Anchorage was 291826

#Ideas for Similar Programs
#•	 Compare data across multiple rows in a spreadsheet.
#•	 Open multiple Excel files and compare data between spreadsheets.
#•	 Check whether a spreadsheet has blank rows or invalid data in any cells and alert the user if it does.
#•	 Read data from a spreadsheet and use it as the input for your Python programs.
