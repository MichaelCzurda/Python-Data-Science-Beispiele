#!python3
#1103_parsing_html_with_beautifulsoup.py - Parsing HTML with the BeautifulSoup Module

#Beautiful Soup is module for extracting information from an HTML page. -> name is bs4(Install: pip install beautifulsoup4, IMport:  import bs4)
#Created example.html!!!

###########################################
#Creating a BeautifulSoup Object from HTML#
###########################################

import requests, bs4
res=requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))

#You can also load an HTML file from your hard drive by passing a File object to bs4.BeautifulSoup()
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))
exampleFile.close()

#Once you have a BeautifulSoup object, you can use its methods to locate specific parts of an HTML document.

#############################################
#Finding an Element with the select() Method#
#############################################

#You can retrieve a web page element from a BeautifulSoup object by calling
#the select()method and passing a string of a CSS selector for the element you
#are looking for. 

#Examples - css selectors
#soup.select('div') 					All elements named <div>
#soup.select('#author') 				The element with an id attribute of author
#soup.select('.notice')					All elements that use a CSS class attribute named notice
#soup.select('div span') 				All elements named <span> that are within an element named <div>
#soup.select('div > span') 				All elements named <span> that are directly within an element named <div>, with no other element in between
#soup.select('input[name]') 			All elements named <input> that have a name attribute with any value
#soup.select('input[type="button"]') 	All elements named <input> that have an attribute named type with value button

#For example, soup.select('p #author') will match any element that
#has an id attribute of author, as long as it is also inside a <p> element.

#The select() method will return a list of Tag objects, which is how
#Beautiful Soup represents an HTML element. The list will contain one
#Tag object for every match in the BeautifulSoup object’s HTML. Tag values
#can be passed to the str() function to show the HTML tags they represent. 

#Tag values also have an attrs attribute that shows all the HTML attributes
#of the tag as a dictionary. 

#With example.html
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
print(type(elems))
#<class 'list'>
print(len(elems))
#1
print(type(elems[0]))
#<class 'bs4.element.Tag'>
print(elems[0].getText())
#Al Sweigart
print(str(elems[0]))
#<span id="author">Al Sweigart</span>
print(elems[0].attrs)
#{'id': 'author'}

#You can also pull all the <p> elements from the BeautifulSoup object. :
pElems = exampleSoup.select('p')
print(str(pElems[0]))
#<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>
print(str(pElems[0].getText()))
#Download my Python book from my website.
print(str(pElems[1]))
#<p class="slogan">Learn Python the easy way!</p>
print(str(pElems[1].getText()))
#Learn Python the easy way!
print(str(pElems[2]))
#<p>By <span id="author">Al Sweigart</span></p>
print(str(pElems[2].getText()))
#By Al Sweigart

#This time, select() gives us a list of three matches

###########################################
#Getting Data from an Element’s Attributes#
###########################################

#The get() method for Tag objects makes it simple to access attribute values
#from an element. The method is passed a string of an attribute name and
#returns that attribute’s value.

soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
print(str(spanElem))
#<span id="author">Al Sweigart</span>
print(str(spanElem.get('id')))
#author
print(spanElem.get('some_nonexistent_addr') == None)
#True
print(spanElem.attrs)
#{'id': 'author'}
