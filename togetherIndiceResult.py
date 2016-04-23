##link all phase one coding together and output the indice result
## By Xi Chen

from QueryWithTF import outputStringQuery
from QueryWithTF import extractValuePart
from lxml import html
from lxml.html.clean import clean_html
import string
import os
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import utils
import codecs # otherwise, it has ascii encoding error
import preprocess
import inverted_index
import candidatefile
import candidateVector
from tfidf_for_Query import tfidf_Query
from similarity import vectorlength
from similarity import simDistance
from similarity import computerSimilarity
import sys


query = sys.argv
query.pop(0)
print query
query = ' '.join(query)
query = preprocess.cleanquery(query)
print query
query = outputStringQuery(query)
print query
#querylist = query.split()
#query = inverted_index.tf_of_query(querylist)
##extract value for the final vectList
#queryTF = extractValuePart(query)

df_file = utils.read_datastructure('df_dictonary.pkl')
#tf_file = utils.read_datastructure('word_dict.pkl')

#queryTFIDF = tfidf_for_Query(query,df_file,tf_file)
queryTFIDF = tfidf_Query(query,df_file)

candidateIndice = candidatefile.candidate_files(query,91)

VectorList = utils.read_datastructure('doc_tfidf_matrix.pkl')
#print candidateIndice

CandidateList = candidateVector.extractCandidates(VectorList, candidateIndice)
#print len(CandidateList[0])
#print len(queryTFIDF)

RankedDocList = computerSimilarity(queryTFIDF, CandidateList,candidateIndice)

print RankedDocList










