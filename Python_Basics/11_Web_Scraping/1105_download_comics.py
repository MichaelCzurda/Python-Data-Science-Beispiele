#!python3
#1105_download_comics.py - Project: Downloading All XKCD Comics

#Blogs and other regularly updating websites usually have a front page with
#the most recent post as well as a Previous button on the page that takes you
#to the previous post. Then that post will also have a Previous button, and so
#on, creating a trail from the most recent page to the first post on the site.
#If you wanted a copy of the site’s content to read when you’re not online,
#you could manually navigate over every page and save each one. But this is
#pretty boring work, so let’s write a program to do it instead.
#XKCD is a popular geek webcomic with a website that fits this structure
#(see Figure 11-6). The front page at http://xkcd.com/ has a Prev button that
#guides the user back through prior comics. Downloading each comic by
#hand would take forever, but you can write a script to do this in a couple of minutes

#Here’s what the program does:
#•	 Loads the XKCD home page.
#•	 Saves the comic image on that page.
#•	 Follows the Previous Comic link.
#•	 Repeats until it reaches the first comic.

#This means the code will need to do the following:
#•	 Download pages with the requests module.
#•	 Find the URL of the comic image for a page using Beautiful Soup.
#•	 Download and save the comic image to the hard drive with iter_content().
#•	 Find the URL of the Previous Comic link, and repeat.

############################
#Step 1: Design the Program#
############################

#•	 The URL of the comic’s image file is given by the href attribute of an <img> element.
#•	 The <img> element is inside a <div id="comic"> element.
#•	 The Prev button has a rel HTML attribute with the value prev.
#•	 The first comic’s Prev button links to the http://xkcd.com/# URL, indicating that there are no more previous pages.

import requests, os, bs4

url = 'http://xkcd.com' #starting url
os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd

while not url.endswith('#'):
# Step 2: Download the Web Page
	print('Downloading page: {}'.format(url))
	res = requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text)
	
# Step 3: Find and Download the Comic Image
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = 'http:' + comicElem[0].get('src')
		print('Downloading image {}...'.format(comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
#Step 4: Save the Image and Find the Previous Comic
		#Save the image to ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
	#Get the Prev buttons url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')

#Ideas for Similar Programs
#Downloading pages and following links are the basis of many web crawling
#programs. Similar programs could also do the following:
#•	 Back up an entire site by following all of its links.
#•	 Copy all the messages off a web forum.
#•	 Duplicate the catalog of items for sale on an online store.

#The requests and BeautifulSoup modules are great as long as you can
#figure out the URL you need to pass to requests.get(). However, sometimes
#this isn’t so easy to find. Or perhaps the website you want your program to
#navigate requires you to log in first. The selenium module will give your programs the power to perform such sophisticated tasks.
