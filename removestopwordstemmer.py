# Author: Yuanwei Wu
# Date: 3/2/2016, 1st version
# Date: 3/5/2016, 2nd version: add the unicode (line24) fixed the EncoderError
# add str() at line54 to fix TypeError: expected a character buffer object
# Description: IR Project: part 1, Document processing and indexing
# Tokenize, remove stop word, stemming
# using NLTK package


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#from nltk.stem.lancaster import LancasterStemmer
# there are many stemmers in nltk, here I use PorterStemmer
from nltk.stem import PorterStemmer
import os
import codecs # otherwise, it has ascii encoding error

ps = PorterStemmer()

def RemoveStopwdStem(inputfolder, outputfolder, url):
	# load the file
	init_file = open(inputfolder+"/"+url,'r')
	init_word = init_file.read()
	init_word = unicode(init_word,'utf-8')
	init_file.close()	
	
	# tokenize
	tokenized_word = word_tokenize(init_word)
	#print(tokenized_word)
	#tokenizedword = len(tokenized_word)
	#print(tokenizedword)
	
	# remove stop words
	stop_words = set(stopwords.words("english"))
	removedstop_word = []
	removedstop_word = [w for w in tokenized_word if not w in stop_words]
	#print(removedstop_word)
	#lengthstopword = len(removedstop_word)
	#print(lengthstopword)

	# stemming
	stemmed_words = []
	for w in removedstop_word:
		stemmed_words.append(ps.stem(w))

	mid_file = open(outputfolder+"/"+url+".removed", "w")
	mid_file.write(str(stemmed_words))
	mid_file.close()


# processing all the files
for filename in os.listdir('cleaned/'):
    print(filename)
    RemoveStopwdStem("cleaned","Removed",filename)
print("Done.")


# test the 1st file in cleaned/
# filename = 'Acadia_National_Park.htm.cleaned'
# RemoveStopwdStem("cleaned","Removed",filename)