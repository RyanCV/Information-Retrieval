#coding=utf-8

# Date:4/27/2016
# Description: build the feeded urls lists with name and urls
import re
from os import listdir
from ast import literal_eval
import utils

feedList = {}
finalList = {}
crawlList = set()
f = open("./CrawledUrlList2.txt", 'r')
content = f.readlines()
for line in content:
	line_tuple = literal_eval(line)#change str to tuple
	crawlList.add(line_tuple)
# print crawlList
for (key,val) in crawlList:
	# print str(key)+'.txt',val
	feedList[str(key)+'.txt'] = val
# print feedList
# write the name and url of crawled and original webpages
foldername = "./feeded_files/"
filenames = listdir(foldername)
# for webpg in filenames:

finalFeedList = dict()
# for (k11,v11) in ff:
for (k22,v22) in feedList.items():
	for webpg in filenames:
		if webpg == k22:
			# print k22, v22
			finalFeedList[webpg] = v22;
		elif webpg[-3:] == 'htm':
			finalFeedList[webpg] = "http://localhost/docsnew/" + webpg
print len(finalFeedList)
# for (k1,v1) in aa.items():
# 	final = open('./finalFeedList.txt', 'a')
# 	final.write(k1 + " " + v1 + "\n")
# 	final.close()

# write to pkl format: dict
# utils.store_datastructure('finalFeedList.pkl',finalFeedList)
finalList = utils.read_datastructure('finalFeedList.pkl')
print finalList

