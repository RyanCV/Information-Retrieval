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
	#os.chdir("./cleaned")
	init_file = open(inputfolder+"/"+url,'r')#this has unicode error
	# init_file = codecs.open(inputfolder+"/"+url,encoding='utf-8')
	init_word = init_file.read()

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
		try:
			stemmed_words.append(str(ps.stem(w)))
		
		except UnicodeDecodeError:
			print w

	outcome = ' '.join(stemmed_words)
	#print(stemmed_words)
	#stemmedword = len(stemmed_words)
	#print(stemmedword)

	# There are some problems on the encoding, I need to figure it out.

	# mid_file = codecs.open(outputfolder+"/"+url, "w") 
	mid_file = open(outputfolder+"/"+url+".removed", "w")
	mid_file.write(outcome)
	mid_file.close()

	# text_file = codecs.open(outputfolder+"/"+url+".removed", "w")
	# text_file = open(outputfolder+"/"+url+".removed", "w")
	# # text_file.write(text.encode('utf-8'))
	# text_file.close()
	# os.remove(outputfolder+"/"+url)


"""
for filename in os.listdir('cleaned/'):
    print(filename)
    if ".DS_Store" == filename:
        continue;
    RemoveStopwdStem("cleaned","Removed",filename)
print("Done.")
"""

# test the 1st file in cleaned/
# filename = 'Acadia_National_Park.htm.cleaned'
# RemoveStopwdStem("cleaned","Removed",filename)
