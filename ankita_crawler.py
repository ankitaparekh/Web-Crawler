#!/usr/bin/env python

import sys
import re
import urllib
import urllib2
import urlparse
import time
from bs4 import BeautifulSoup


#if true present else not present
def isLinkPresent(url,visited_array):
	va = [item.lower() for item in visited_array]
	if url.lower() in va:
		return True
	else:
		return False;

#get the input from user
if len(sys.argv) == 3:
	baseUrl = sys.argv[1]
	keyPhrase = sys.argv[2]
	isFocused = True
elif len(sys.argv) == 2:
	isFocused = False
	baseUrl = sys.argv[1]
else:
	print("wrong input format")
	isFocused = False

initDepth = 1

# checks
colon = ":"
hashes = "#"
mainPage = "http://en.wikipedia.org/wiki/Main_Page"
startsUrl = "http://en.wikipedia.org/wiki/"

if isFocused:
	print "this is a focused crawler"
	#construct the regex for keyphrase
	keyPhrase_regex="\\b" + keyPhrase + "\\b"
else:
	print "this is an unfocused crawler"

urlList = [[baseUrl, initDepth]]
visitedLinks = [baseUrl]


#keep looping till the depth is less than 3
while urlList[0][1] < 3:
	try:
		rawText = urllib.urlopen(urlList[0][0]).read()
	except:
		# if any error this thing gets printed
		print "error"
		print urlList[0][0]

	soup = BeautifulSoup(rawText)
	#call Function to check for attribute rel='canonical'
	canonical = soup.find("link", rel="canonical")
	if canonical:
		canonical_url = canonical['href']

	if not isLinkPresent(canonical_url, visitedLinks):
		visitedLinks.append(canonical_url)

	url_depth=urlList[0][1]
	#print("depth is: ",url_depth)
	#update the depth
	url_depth = url_depth + 1
	#print("depth for next level is: ", url_depth)
	urlList.pop(0)
	count_depth = 0
	#check if the crawler is focused or not
	if isFocused:
		if soup.find_all(text = re.compile(keyPhrase_regex, re.IGNORECASE)):
			for aTag in soup.findAll('a', href= True):
				current_url = aTag['href']
				concatUrl = urlparse.urljoin(baseUrl, current_url)
				# check if the url starts with startUrl
				if concatUrl.startswith(startsUrl):
					#proceed only if it is not a main page
					if not mainPage in concatUrl:
						# ignore if : is present
						if colon not in current_url:
							#split the url if hash is present
							concatUrl = concatUrl.split(hashes,1)[0]
							#ignore if the url is already visited
							if not isLinkPresent(concatUrl, visitedLinks):
								#open the page to look for keyPhrase
								openCurrPage = urllib2.urlopen(concatUrl)
								currentSoup = BeautifulSoup(openCurrPage.read())
								if currentSoup.find_all(text = re.compile(keyPhrase_regex, re.IGNORECASE)):
                                    					c = currentSoup.find('link',{"rel":"canonical"})
									if c :
                                    						canonical_link_data = c['href']
									else :
										canonical_link_data = concatUrl

                                    					if not isLinkPresent(canonical_link_data,visitedLinks):
                                        					visitedLinks.append(canonical_link_data)
                                        					urlList.append([concatUrl,url_depth])

	else:
		for aTag in soup.findAll('a', href= True):
				current_url = aTag['href']
				concatUrl = urlparse.urljoin(baseUrl, current_url)
				# check if the url starts with startUrl
				if concatUrl.startswith(startsUrl):
					#proceed only if it is not a main page
					if not mainPage in concatUrl:
						# ignore if : is present
						if colon not in current_url:
							#split the url if hash is present
							concatUrl = concatUrl.split(hashes,1)[0]
							#ignore if the url is already visited
							if not isLinkPresent(concatUrl, visitedLinks):
								#print(visitedLinks)
                                				#open the page to look for keyPhrase
								openCurrPage = urllib2.urlopen(concatUrl)
								cur_Soup = BeautifulSoup(openCurrPage.read())
                                				c = cur_Soup.find('link',{"rel":"canonical"})
								if c :
                                    					canonical_link_data = c['href']
								else :
									canonical_link_data = concatUrl
								#unfocused crawling
								#append this link to list of visited urls
                                				if not isLinkPresent(canonical_link_data,visitedLinks):
								    visitedLinks.append(canonical_link_data)
								    #append this link to the urlList also
								    urlList.append([concatUrl,url_depth])
	time.sleep(1)								
					
	
	
for aa in visitedLinks:
	print aa

print "Total number of visited Links: " , len(visitedLinks)