# -*- coding: utf-8 -*-
from lxml import html
from lxml.html.clean import clean_html
import string
import os

def checkpuc(ch):
    if ch.isalnum():
        return ch
    else:
        return ' '

#delete html tags, remove puncs and convert to lowercase
#all cleaned pages are stored in folder 'cleaned'
def cleanpage(infolder,outfoler,url):
    
    init_file = open(infolder+"/"+url,'r')
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
        cleanpage("docsnew","cleaned",filename)

#cleanallpage('docsnew/')
#print("Done.")