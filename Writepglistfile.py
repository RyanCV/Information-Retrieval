# Description: write the contents in DownloadPgList.txt without same contents in increasing order
# Date: 4/22/2016
# Author: Yuanwei Wu
import os,re

# read the file
fold = open('DownloadPgList.txt', 'r')
content = fold.readlines()
lineset = set()
linelist = []
linetuple = ()
# set can't have same information
for line in content:
	lineset.add(line)
# read each line, separate the number and url to a list
# then, put the separated two elements into tuple
# element 0 is str, need to change to number
for line2 in lineset:
	mid = line2.split(' ')
	urlCnt = int(mid[0]) # need to be float/int, the original is str
	# urlName = str(mid[1]) # need to be str, the orginal is str, no need to change 
	linetuple = (urlCnt, mid[1])
	linelist.append(linetuple)
# sort the linelist which is list of tuple
finalline = sorted(linelist, key=lambda x: x[0]) # set the parameters for sorted

# write the sorted url lists into file
for line3 in finalline:
	# print line3
	fnew = open('DownloadNewList.txt', 'a')
	fnewline = fnew.write(str(line3)+'\n')# need to change line3 to str
	# fnewline.close() # need to comment this, otherwise error

