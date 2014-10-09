Web-Crawler
===========

Consists of focused and unfocused web crawler that crawls pages till depth 3.

This program takes in the seed document url and optional keyphrase as an input.Depending on the input it will crawl all the urls
till depth 3.


Instructions on how to (compile and) run the code:
===================================================

My program needs BeautifulSoup Library.I have assumed that it is already installed.

To run the program:

1.For focused crawling run the following command:
-------------------------------------------------

$python ankita_crawler.py http://en.wikipedia.org/wiki/Gerard_Salton 'Information Retrieval' > focused_result.txt
(The results will be saved in focused_result.txt )

If you want to view the results on the terminal then execute the following command:
$python ankita_crawler.py http://en.wikipedia.org/wiki/Gerard_Salton 'Information Retrieval'
(The results will be shown on the terminal.)

2.For unfocused crawling run the following command:
-------------------------------------------------

$python ankita_crawler.py http://en.wikipedia.org/wiki/Gerard_Salton > unfocused_result.txt
(The results will be saved in unfocused_result.txt)

If you want to view the results on the terminal then execute the following command:
$python ankita_crawler.py http://en.wikipedia.org/wiki/Gerard_Salton the results will be shown on the terminal.
￼￼￼￼
