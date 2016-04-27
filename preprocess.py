# -*- coding: utf-8 -*-
from lxml import html
from lxml.html.clean import clean_html
import string
import os
import utils

def checkpuc(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '

#delete html tags, remove puncs and convert to lowercase
#all cleaned pages are stored in folder 'cleaned'
def cleanpage(infolder,outfoler,url):
    
    if ".DS_Store" == url:
        return
    init_file = open(infolder+url,'r')
    init_str = init_file.read()
    init_file.close()
    init_str = init_str.replace('</',' </');
    #print(init_str)
    
    
    mid_file = open(outfoler+"/"+url, "w")
    mid_file.write(init_str)
    mid_file.close()
    
    tree = html.parse(outfoler+"/"+url)
    tree = clean_html(tree)
    text = tree.getroot().text_content()
    text = ''.join(checkpuc(ch) for ch in text)
    text = ' '.join(text.split())
    text = text.lower()
    text_file = open(outfoler+"/"+url+".cleaned", "w")
    text_file.write(text.encode('utf-8'))
    text_file.close()
    os.remove(outfoler+"/"+url)

#preprocess query string
def cleanquery(query):
    text = ''.join(checkpuc(ch) for ch in query)
    text = ' '.join(text.split())
    text = text.lower()
    return text

def cleanallpage(path):
    for filename in os.listdir(path):
        print(filename)
        cleanpage(path,"cleaned",filename)

def getpath_of_files():
    path_list = []
    for filename in os.listdir('ku_crawled_files/'):
        path_list.append(os.path.abspath("ku_crawled_files/"+filename))
    for filename in os.listdir('docsnew/'):
        path_list.append(os.path.abspath("docsnew/"+filename))
    print path_list
    utils.store_datastructure('filepath_list.pkl',path_list)

#cleanallpage('docsnew/')
#cleanallpage('ku_crawled_files/')
#getpath_of_files()
#print("Done.")

