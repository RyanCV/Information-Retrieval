# Xi Chen
# 3/16/2016
# Let user input a query and then do tokenize, remove stop word and stemming on the string
# Also output the tf list for query


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
    #return a list instead of returning str
    outcome = outcome.split()

    return outcome

def extractValuePart(query):
    values=[]
    for a,b in query:
        values.append(b)
    return values

"""
## the query terms after preprocess

query = raw_input('Enter your query:')
query = preprocess.cleanquery(query)
query = outputStringQuery(query)

## output a vectors list contain the tf values for query (0 or 1)
querylist = query.split()

queryTF = inverted_index.tf_of_query(querylist)

#print query
"""
