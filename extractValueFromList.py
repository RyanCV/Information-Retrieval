# Xi Chen

from QueryWithDF import outputStringQuery
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


def extractValuePart(query):
    values=[]
    for a,b in query:
        values.append(b)
    return values

'''
query = raw_input('Enter your query:')
query = preprocess.cleanquery(query)
query = outputStringQuery(query)
querylist = query.split()
query = inverted_index.tf_of_query(querylist)

newList = extractValuePart(query)

print newList
'''