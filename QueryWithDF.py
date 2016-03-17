# Xi Chen
# 3/16/2016
# Let user input a query and then do tokenize, remove stop word and stemming on the string


from lxml import html
from lxml.html.clean import clean_html
import string
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import codecs # otherwise, it has ascii encoding error
import preprocess
import inverted_index


def outputStringQuery(query):
    ps = PorterStemmer()
    #tokenize query
    tokenized_word = word_tokenize(query)
    #remove stop word
    stop_words = set(stopwords.words("english"))
    removedstop_word = []
    removedstop_word = [w for w in tokenized_word if not w in stop_words]
    #stemming query
    stemmed_words = []
    for w in removedstop_word:
        try:
            stemmed_words.append(str(ps.stem(w)))

        except UnicodeDecodeError:
            print w

    outcome = ' '.join(stemmed_words)

    return outcome


query = raw_input('Enter your query:')
query = preprocess.cleanquery(query)
query = outputStringQuery(query)
querylist = query.split()
query = inverted_index.tf_of_query(querylist)

#print query

