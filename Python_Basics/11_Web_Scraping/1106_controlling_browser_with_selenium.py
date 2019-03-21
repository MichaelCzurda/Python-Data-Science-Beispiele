#!python3
#1106_controlling_browser_with_selenium.py - Controlling the Browser with the selenium Module

#The selenium module lets Python directly control the browser by programmatically 
#clicking links and filling in login information, almost as though there is a human user interacting with the page. 

########################################
#Starting a Selenium-Controlled Browser#
########################################
#Importing the modules for Selenium is slightly tricky. Instead of import
#selenium, you need to run from selenium import webdriver. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#ACHTUNG chromedriver.exe im Ordner ablegen

#Chrome Option - Browser nicht öffnen
#options = webdriver.ChromeOptions()
#options.add_argument('headless')

browser = webdriver.Chrome()
print(type(browser))
#<class 'selenium.webdriver.chrome.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')

##############################
#Finding Elements on the Page#
##############################
#WebDriver objects have quite a few methods for finding elements on a
#page. They are divided into the find_element_* and find_elements_* methods.
#The find_element_* methods return a single WebElement object, representing
#the first element on the page that matches your query. The find_elements_*
#methods return a list of WebElement_* objects for every matching element on
#the page

#Examples:
#browser.find_element_by_class_name(name)
#browser.find_elements_by_class_name(name)	Elements that use the CSS class name

#browser.find_element_by_css_selector(selector)
#browser.find_elements_by_css_selector(selector) Elements that match the CSS selector

#browser.find_element_by_id(id)
#browser.find_elements_by_id(id) Elements with a matching id attribute value

#browser.find_element_by_link_text(text)
#browser.find_elements_by_link_text(text) <a> elements that completely match the text provided

#browser.find_element_by_partial_link_text(text)
#browser.find_elements_by_partial_link_text(text) <a> elements that contain the text provided

#browser.find_element_by_name(name)
#browser.find_elements_by_name(name) Elements with a matching name attribute value

#browser.find_element_by_tag_name(name)
#browser.find_elements_by_tag_name(name) Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')

# If no elements exist on the page that match what the method is looking for, the selenium module raises a NoSuchElement exception. 

#Once you have the WebElement object, you can find out more about it by
#reading the attributes or calling the methods

#tag_name 				The tag name, such as 'a' for an <a> element
#get_attribute(name) 	The value for the element’s name attribute
#text 					The text within the element, such as 'hello' in <span>hello</span>
#clear() 				For text field or text area elements, clears the text typed into it
#is_displayed() 		Returns True if the element is visible; otherwise returns False
#is_enabled() 			For input elements, returns True if the element is enabled; otherwise returns False
#is_selected() 			For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
#location 				A dictionary with keys 'x' and 'y' for the position of the element in the page

#Example:
elem = browser.find_element_by_class_name('card-block')
print('Found <%s> element with that class name!' % (elem.tag_name))
#Found <div> element with that class name!

###################
#Clicking the Page#
###################
#WebElement objects returned from the find_element_* and find_elements_*
#methods have a click() method that simulates a mouse click on that element. 
#This method can be used to follow a link, make a selection on a radio
#button, click a Submit button, or trigger whatever else might happen when
#the element is clicked by the mouse. 
#Example:
linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
#<class 'selenium.webdriver.remote.webelement.WebElement'>
linkElem.click()
#<a href="https://automatetheboringstuff.com/" class="btn btn-primary">Read Online for Free</a>

##################################
#Filling Out and Submitting Forms#
##################################
#Sending keystrokes to text fields on a web page is a matter of finding the <input>
#or <textarea> element for that text field and then calling the send_keys() method. 
#Example:
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my-real_email')
emailElem.submit()
# Calling the submit() method on any element will have the same result as clicking 
#the Submit button for the form that element is in. 

######################
#Sending special keys#
######################
#Selenium has a module for keyboard keys that are impossible to type into a
#string value, which function much like escape characters. These values are
#stored in attributes in the selenium.webdriver.common.keys module. Since that
#is such a long module name, it’s much easier to run from selenium.webdriver
#.common.keys import Keys at the top of your program; if you do, then you can
#simply write Keys anywhere you’d normally have to write selenium.webdriver
#.common.keys. 

#Commonly used:
#Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT			The keyboard arrow keys
#Keys.ENTER, Keys.RETURN 							The enter and return keys
#Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP	The home, end, pagedown, and pageup keys
#Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE			The esc, backspace, and delete keys
#Keys.F1, Keys.F2, ... , Keys.F12 					The F1 to F12 keys at the top of the keyboard
#Keys.TAB 											The tab key

#For example, if the cursor is not currently in a text field, pressing the
#home and end keys will scroll the browser to the top and bottom of the page,
#respectively:

from selenium.webdriver.common.keys import Keys
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) #scrolls to bottom
htmlElem.send_keys(Keys.HOME) #scrolls to top

#The <html> tag is the base tag in HTML files: The full content of the
#HTML file is enclosed within the <html> and </html> tags. Calling browser
#.find_element_by_tag_name('html') is a good place to send keys to the general
#web page. This would be useful if, for example, new content is loaded once
#you’ve scrolled to the bottom of the page.

##########################
#Clicking Browser Buttons#
##########################
#Selenium can simulate clicks on various browser buttons as well through the following methods:
#browser.back() Clicks the Back button.
#browser.forward() Clicks the Forward button.
#browser.refresh() Clicks the Refresh/Reload button.
#browser.quit() Clicks the Close Window button

##################
#More information#
##################
#Selenium can do much more beyond the functions described here. It can
#modify your browser’s cookies, take screenshots of web pages, and run
#custom JavaScript. To learn more about these features, you can visit the
#Selenium documentation at http://selenium-python.readthedocs.org/.

####################
#Project:PLay 20148#
####################

browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
while True:
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)
	
