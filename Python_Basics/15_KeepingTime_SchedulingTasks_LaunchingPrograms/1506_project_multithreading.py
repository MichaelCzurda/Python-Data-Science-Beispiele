#! python3
#1506_project_multithreading.py - Project: Multithreaded XKCD Downloader

#In Chapter 11, you wrote a program that downloaded all of the XKCD
#comic strips from the XKCD website. This was a single-threaded program:
#It downloaded one comic at a time. Much of the program’s running time
#was spent establishing the network connection to begin the download and
#writing the downloaded images to the hard drive. If you have a broadband
#Internet connection, your single-threaded program wasn’t fully utilizing the
#available bandwidth.
#A multithreaded program that has some threads downloading comics
#while others are establishing connections and writing the comic image files
#to disk uses your Internet connection more efficiently and downloads the
#collection of comics more quickly.

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd

##############################################
#Step 1: Modify the Program to Use a Function#
##############################################

def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		#Download the Page
		print('Downloading page http://xkcd.com/%s...' % (urlNumber))
		res = requests.get('http://xkcd.com/%s' % (urlNumber))
		res.raise_for_status()
		
		soup = bs4.BeautifulSoup(res.text)
		
		#Find and Download the Comic Image
		comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = 'http:' + comicElem[0].get('src')
		print('Downloading image {}...'.format(comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
		#Save the image to ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

##################################
#Step 2: Create and Start Threads#
##################################
downloadThreads=[] # a list of all the Thread objects
for i in range(0, 300, 100): # loops 14 times, creates 14 threads
	downloadThread=threading.Thread(target=downloadXkcd, args=(i, i + 99))
	downloadThreads.append(downloadThread)
	downloadThread.start()

#First we make an empy list downloadThreads; the list will help us keep track
#of the many Thread objects we’ll create. Then we start our for loop. Each time
#through the loop, we create a Thread object with threading.Thread(), append
#the Thread object to the list, and call start() to start running downloadXkcd()
#in the new thread. Since the for loop sets the i variable from 0 to 500 at steps
#of 100, i will be set to 0 on the first iteration, 100 on the second iteration, 200
#on the third, and so on. Since we pass args=(i, i + 99) to threading.Thread(),
#the two arguments passed to downloadXkcd() will be 0 and 99 on the first iteration, 
#100 and 199 on the second iteration, 200 and 299 on the third, and so on.
#As the Thread object’s start() method is called and the new thread
#begins to run the code inside downloadXkcd(), the main thread will continue
#to the next iteration of the for loop and create the next thread.

#####################################
#Step 3: Wait for All Threads to End#
#####################################
## Wait for all threads to end.
for downloadThread in downloadThreads:
	downloadThread.join()
print('Done.')

#The 'Done.' string will not be printed until all of the join() calls have
#returned. If a Thread object has already completed when its join() method
#is called, then the method will simply return immediately. If you wanted to
#extend this program with code that runs only after all of the comics downloaded, 
#you could replace the print('Done.') line with your new code.
