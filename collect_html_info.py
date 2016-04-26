# -*- coding: utf-8 -*-
# Yang Tian
import string
import os

def read_index(path):
    index_file = open('CrawledUrlList2.txt','r')

    index_file.close()

def cleanhtmlpages(path):
    for filename in os.listdir(path):
        print(filename)
        #cleanpage("docsnew","cleaned",filename)

cleanhtmlpages('ku_crawled_files/')
#print("Done.")