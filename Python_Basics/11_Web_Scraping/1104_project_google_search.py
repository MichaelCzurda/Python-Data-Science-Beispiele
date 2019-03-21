#!python3
#1104_project_google_search.py - Project: “I’m Feeling Lucky” Google Search

#Whenever I search a topic on Google, I don’t look at just one search result
#at a time. By middle-clicking a search result link (or clicking while holding ctrl), 
#I open the first several links in a bunch of new tabs to read later. 

#automate this workflow
#search term to command line -> open a browser with all top search results

#This is what the program does:
#•	 Gets search keywords from the command line arguments.
#•	 Retrieves the search results page.
#•	 Opens a browser tab for each result.

#This means the code will need to do the following:
#•	 Read the command line arguments from sys.argv.
#•	 Fetch the search result page with the requests module.
#•	 Find the links to each search result.
#•	 Call the webbrowser.open() function to open the web browser.

####################################################################
#Step 1: Get the Command Line Arguments and Request the Search Page#
####################################################################

#the search result page on google has a URL like: 
	# https://www.google.com/search?q=SEARCH_TERM_HERE
#The requests module can download this page and then you can use Beautiful Soup 
#to find the search result links in the HTML.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

##############################
#Step 2: Find All the Results#
##############################
#Ingest search results in the browser
# You just need to find the pattern that all the search result links have. But this <a> element 
#doesn’t have anything that easily distinguishes it from the nonsearch result <a> elements on the page.

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')

#If you look up a little from the <a> element, though, there is an element
#like this: <h3 class="r">. Looking through the rest of the HTML source,
#it looks like the r class is used only for search result links. You don’t have
#to know what the CSS class r is or what it does. You’re just going to use
#it as a marker for the <a> element you are looking for. You can create a
#BeautifulSoup object from the downloaded page’s HTML text and then use
#the selector '.r a' to find all <a> elements that are within an element that
#has the r CSS class.

###########################################
#Step 3: Open Web Browsers for Each Result#
###########################################

# Open a browser tab for each result.
numOpen = min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))


# Note that the href attribute’s value in the returned <a> elements do not have 
#the initial http://google.com part, so you have to
#concatenate that to the href attribute’s string value.


#Ideas for Similar Programs
#The benefit of tabbed browsing is that you can easily open links in new tabs
#to peruse later. A program that automatically opens several links at once
#can be a nice shortcut to do the following:
#•	 Open all the product pages after searching a shopping site such as Amazon
#•	 Open all the links to reviews for a single product
#•	 Open the result links to photos after performing a search on a photo site such as Flickr or Imgur
