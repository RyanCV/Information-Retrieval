#_*_coding: utf-8 _*_


import urllib2, urllib, urlparse
import os, sys
from HTMLParser import HTMLParser
import threading, Queue
reload(sys)
sys.setdefaultencoding('utf-8')

# get the domain name: not in url, then dismiss this url
def get_net_location(url):
	find_net_loc = urlparse.urlparse(url).netloc
	url_split = find_net_loc.split('.')
	# return ku.edu only
	domain_name = url_split[-2] + '.' + url_split[-1]
	return domain_name


class MyHTMLParser(HTMLParser):
	def __init__(self, hmpage, domain):
		HTMLParser.__init__(self)
		self.hmpage = hmpage
		self.domain = domain
		self.page_links = set()
	def handle_starttag(self, tag, attrs):
	       	if cmp(tag, 'a') == 0:
	        	for (key, value) in attrs:
	        		if cmp(key, 'href') == 0:
	        			links = urlparse.urljoin(self.hmpage, value)
	        			self.page_links.add(links)
	def get_page_html(self, url):
		global queue
		global ToCrawl
		global HasCrawled
		try:
			pageReq = urllib2.Request(url)
			req_header = urllib2.urlopen(pageReq).info().getheader('Content-Type')
			if 'text/html' in req_header:
				pageHtml = urllib2.urlopen(url).read()# after reload(sys), no need to use read().decode('utf-8')
				self.feed(pageHtml)
				for pglink in self.page_links:
					if (pglink in ToCrawl) or (pglink in HasCrawled):
						continue
					try:
						if self.domain != get_net_location(pglink):
							continue
					except:
						print "Can't find domain name in current url!"
						continue
					if 'mailto' in pglink:
						continue
					if 'tel:' in pglink:
						continue
					if '.pdf' in pglink:
						continue
					queue.put(pglink)
					ToCrawl.add(pglink)
				return pageHtml
			else:
				print "It's not url for text or html."
				return " "
		except Exception as e:
			print str(e)
	def handle_endtag(self, tag):
		pass
# The spider function
def MySpider(url):
	global queue
	global ToCrawl
	global HasCrawled
	global HasDownloadpg # set()
	global DownloadPgList # list
	global pgCount
	NewLink = url
	while len(ToCrawl) > 0:
		if NewLink in HasCrawled or NewLink in HasDownloadpg:
			NewLink = queue.get()
			continue
		HasCrawled.add(NewLink)
		print "HasCrawled:", len(HasCrawled), " ToCrawl:", len(ToCrawl)
		print "now crawling:", NewLink
		try:	
			pgpaser = MyHTMLParser(homepage, domain)
			pghtml = pgpaser.get_page_html(NewLink)
			try:
				HasDownloadpg.add(NewLink)
				pgCount = len(HasDownloadpg)
				dwldpg = [pgCount, NewLink]
				DownloadPgList.append(dwldpg)
				print "Downloading...", NewLink
				f = open('./ku_crawled_files/'+'%d.txt' % pgCount, 'w')
				f.write(pghtml)
				f.close()
				# also write the pgCount + NewLink to file 
				for (key,val) in DownloadPgList:
					fpg = open('DownloadPgList.txt', 'a')
					fpg.write("%s %s \n" % (key,val))
					fpg.close()
				print "Successful download ", NewLink, "download page number:", len(HasDownloadpg)
			except:
				print "Failed to download", NewLink
				continue
			NewLink = queue.get()
		except Exception, e:
			NewLink = queue.get()
			continue


# # The main function to run my web crawler
if __name__ == "__main__":
	# lock = threading.Lock()
	homepage = 'http://www.ku.edu'
	seed = 'http://www.ku.edu'
	domain = get_net_location(homepage)
	global queue
	global ToCrawl
	global HasCrawled
	global HasDownloadpg 
	global DownloadPgList
	global pgCount
	queue = Queue.Queue()
	ToCrawl = set()
	HasCrawled = set()
	HasDownloadpg = set()
	DownloadPgList = []
	pgCount = 0
	ThreadNum = 2
	ThreadList = []

	HasCrawled.add(seed)
	seedpaser = MyHTMLParser(homepage, domain)
	seedpghtml = seedpaser.get_page_html(seed)
	for i in range(0, ThreadNum):
		th = threading.Thread(target = MySpider, args = (queue.get(), ))
		ThreadList.append(th)

	for t in ThreadList:
		t.start()
	print "\n Thread Count %s" % str(threading.activeCount())
	print threading.enumerate()
