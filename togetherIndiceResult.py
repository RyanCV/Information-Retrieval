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
import csv
from utils import *
from minWindow import smallestWindow
from minWindow import newRankedList
import locate_terms
from relevance_feedback import newQuery
import numpy as np

def together_indice_result(query_string,pageno):
    #query = sys.argv
    #query.pop(0)
    #print query
    #query = ' '.join(query)
    pageno = int(pageno)
    query = preprocess.cleanquery(query_string)
    #print query
    query = outputStringQuery(query)
    #print query
    #querylist = query.split()
    #query = inverted_index.tf_of_query(querylist)
    ##extract value for the final vectList
    #queryTF = extractValuePart(query)

    
    #df_file = utils.read_datastructure('df_dictonary.pkl')


    #queryTFIDF = tfidf_for_Query(query,df_file,tf_file)
    

    candidateIndice = candidatefile.candidate_files(query,get_ir_doc_number())
    
    if candidateIndice == []:
        return []
    
    queryTFIDF = tfidf_Query(query,get_ir_df_dictionary())

    #VectorList = utils.read_datastructure('doc_tfidf_matrix.pkl')

    #VectorList = utils.read_datastructure('doc_tfidf_normalize.pkl')
    
    #print 'length'
    #print VectorList[10]
    #print candidateIndice

    CandidateList = candidateVector.extractCandidates(get_ir_tfidf_matrix(), candidateIndice)
    #print len(CandidateList[0])
    #print len(queryTFIDF)

    RankedDocList = computerSimilarity(queryTFIDF, CandidateList,candidateIndice)

    
    full_path_list = get_ir_file_path_list()
    path_list = [full_path_list[i] for i in RankedDocList[0]]
    
    #print RankedDocList[0]
    plen = len(path_list)
    #print(plen)
    if plen == 0:
        return []
    pagecount = plen/20
    lastpage = plen%20
    if(lastpage != 0):
        pagecount+=1
    init_item = (pageno-1)*20
    if pageno != pagecount:
        end_item = init_item+20
    else:
        if lastpage != 0:
            end_item = init_item+lastpage
        else:
            end_item = init_item+20
    part_path_list = path_list[init_item:end_item]
    part_docid_list = RankedDocList[0][init_item:end_item]
    #print part_docid_list
    highlighted_list,highlighted_str_list = locate_terms.locate_terms_indocs(query,part_docid_list)
    allresults_count = [plen]*len(highlighted_list)
    #print(part_path_list)
    #print(highlighted_list)
    return zip(part_path_list,highlighted_list,highlighted_str_list,allresults_count)


#init_all_data()
#print("Loaded")
#together_indice_result('Carlsbad Caverns',1)


def together_indice_result2(query_string,pageno):
    #query = sys.argv
    #query.pop(0)
    #print query
    #query = ' '.join(query)
    pageno = int(pageno)
    query = preprocess.cleanquery(query_string)
    #print query
    query = outputStringQuery(query)
    #print query
    #querylist = query.split()
    #query = inverted_index.tf_of_query(querylist)
    ##extract value for the final vectList
    #queryTF = extractValuePart(query)

    
    #df_file = utils.read_datastructure('df_dictonary.pkl')


    #queryTFIDF = tfidf_for_Query(query,df_file,tf_file)
    

    candidateIndice = candidatefile.candidate_files(query,get_ir_doc_number())
    
    if candidateIndice == []:
        return []
    
    queryTFIDF = tfidf_Query(query,get_ir_df_dictionary())

    #VectorList = utils.read_datastructure('doc_tfidf_matrix.pkl')

    #VectorList = utils.read_datastructure('doc_tfidf_normalize.pkl')
    
    #print 'length'
    #print VectorList[10]
    #print candidateIndice

    CandidateList = candidateVector.extractCandidates(get_ir_tfidf_matrix(), candidateIndice)
    #print len(CandidateList[0])
    #print len(queryTFIDF)

    RankedDocList = computerSimilarity(queryTFIDF, CandidateList,candidateIndice)
    
    docs = get_ir_preprocessed_docs_list()

    proximityResult = newRankedList(docs, RankedDocList, query)
    
    #print proximityResult

    
    full_path_list = get_ir_file_path_list()
    path_list = [full_path_list[i] for i in proximityResult[0]]
    
    #print proximityResult[0]
    plen = len(path_list)
    #print(plen)
    if plen == 0:
        return []
    pagecount = plen/20
    lastpage = plen%20
    if(lastpage != 0):
        pagecount+=1
    init_item = (pageno-1)*20
    if pageno != pagecount:
        end_item = init_item+20
    else:
        if lastpage != 0:
            end_item = init_item+lastpage
        else:
            end_item = init_item+20
    part_path_list = path_list[init_item:end_item]
    part_docid_list = proximityResult[0][init_item:end_item]
    #print part_docid_list
    highlighted_list,highlighted_str_list = locate_terms.locate_terms_indocs(query,part_docid_list)
    allresults_count = [plen]*len(highlighted_list)
    #print(part_path_list)
    #print(highlighted_list)
    return zip(part_path_list,highlighted_list,highlighted_str_list,allresults_count)




#init_all_data()
#print("Loaded")
#together_indice_result2('Kansas History',1)

def together_indice_result3(query_string,pageno,rankedRelevance):
    #query = sys.argv
    #query.pop(0)
    #print query
    #query = ' '.join(query)
    pageno = int(pageno)
    rankedRelevance = [int(x) for x in rankedRelevance]
    #print rankedRelevance
    
    query = preprocess.cleanquery(query_string)
    #print query
    query = outputStringQuery(query)
    #print query
    #querylist = query.split()
    #query = inverted_index.tf_of_query(querylist)
    ##extract value for the final vectList
    #queryTF = extractValuePart(query)

    
    #df_file = utils.read_datastructure('df_dictonary.pkl')


    #queryTFIDF = tfidf_for_Query(query,df_file,tf_file)
    
    

    candidateIndice = candidatefile.candidate_files(query,get_ir_doc_number())
    
    if candidateIndice == []:
        return []
    
    queryTFIDF = tfidf_Query(query,get_ir_df_dictionary())
    #VectorList = utils.read_datastructure('doc_tfidf_matrix.pkl')

    #VectorList = utils.read_datastructure('doc_tfidf_normalize.pkl')
    
    #print 'length'
    #print VectorList[10]
    #print candidateIndice

    CandidateList = candidateVector.extractCandidates(get_ir_tfidf_matrix(), candidateIndice)
    #print len(CandidateList[0])
    #print len(queryTFIDF)
    
    RankedDocList = computerSimilarity(queryTFIDF, CandidateList,candidateIndice)
    
    docs = get_ir_preprocessed_docs_list()

    b4feedback = newRankedList(docs, RankedDocList, query)
    

    releIndex = np.array([n for n,j in enumerate(rankedRelevance) if j==1])
    
    irreleIndex = np.array([n for n,j in enumerate(rankedRelevance) if j ==2])
    
    releIndex = 20*(pageno-1) + releIndex
    irreleIndex = 20*(pageno-1) +irreleIndex
    
    
    realRindex = [b4feedback[0][i] for i in releIndex]
    realIrindex = [b4feedback[0][i] for i in irreleIndex]
    #print realIrindex
    
    
    doc_vectors = get_ir_tfidf_matrix()
    
    releDocs =[doc_vectors[i] for i in realRindex]
    irreleDocs =[doc_vectors[i] for i in realIrindex]
    #print releDocs
    #print type(releDocs)
    
    ### here need users to select relevant and irrelevant sites
    #releDoc = [CandidateList[i] for i in range(0,10)]
    #irreleDoc = [CandidateList[i] for i in range (11,20)]
    
    #print len(releDocs)
    #print len(irreleDocs)
    newQueryTFIDF = newQuery(queryTFIDF, releDocs, irreleDocs)
    #print queryTFIDF == newQueryTFIDF
    newRankedDocList = computerSimilarity(newQueryTFIDF, CandidateList,candidateIndice)
    
    
    docs = get_ir_preprocessed_docs_list()


    relevant_feedback = newRankedList(docs, newRankedDocList, query)
    #print "11111", b4feedback[0]
    #print "22222", relevant_feedback[0]

    
    full_path_list = get_ir_file_path_list()
    path_list = [full_path_list[i] for i in relevant_feedback[0]]
    
    #print relevant_feedback[0]
    plen = len(path_list)
    #print(plen)
    if plen == 0:
        return []
    pagecount = plen/20
    lastpage = plen%20
    init_item = (pageno-1)*20
    if pageno != pagecount:
        end_item = init_item+20
    else:
        if lastpage != 0:
            end_item = lastpage
        else:
            end_item = init_item+20
    part_path_list = path_list[init_item:end_item]
    part_docid_list = relevant_feedback[0][init_item:end_item]
    #print part_docid_list
    highlighted_list,highlighted_str_list = locate_terms.locate_terms_indocs(query,part_docid_list)
    allresults_count = [plen]*len(highlighted_list)
    #print(part_path_list)
    #print(highlighted_list)
    return zip(part_path_list,highlighted_list,highlighted_str_list,allresults_count)

#init_all_data()
#print("Loaded")
#together_indice_result3('wheels',1, [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
