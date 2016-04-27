# Author: Yuanwei Wu & Yang
# Date: 3/16/2016, recove 3/22/2016, revised 4/3/2016, update normalize: 4/23/2016
# Description: input: tf, df in list, 
# output: calculate idf= log10(N/df), only output tf*idf in list

import math
import utils

#by Yang Tian
def tfidf_weight_calculation(tf_dic,df_dic,boolean_dic,doc_num):
    tfidf_dic = {}
    for key,value in tf_dic.iteritems():
        #print key
        tfidf_dic[key] = [ x*math.log10(float(doc_num)/df_dic[key]) for x in value]
    tfidf = sorted([(k,v) for k,v in tfidf_dic.items()])
    
    # # change the tfidt into list, remove the keys
    tfidf_lst = list()
    for k3,v3 in tfidf:
        tfidf_lst.append(v3)
    ## save the tfidf: remove the key, and each list in represents a document vector
    tfidf_doc = list(map(list, zip(*tfidf_lst)))
    utils.store_datastructure('tfidf_matrix.pkl',tfidf_dic)
    """df_list = sorted(df_dic.items())
    tfidf_list = sorted(tfidf_dic.items())
    boolean_list = sorted(boolean_dic.items())
    term_info = []
    df_info = []
    tf_info = []
    bool_info = []
    for x in df_list:
        term_info.append(x[0])
        df_info.append(x[1])
    for y in tfidf_list:
        tf_info.append(y[1])
    for z in boolean_list:
        bool_info.append(z[1])
    tuple_info = zip(term_info,df_info,bool_info,tf_info)
    #utils.writedic_to_csv(tuple_info,'tfdf_info.csv')"""


def tf_idf_calculation(tf, df):
	tfidf = dict()
	idf = dict()
	tffile_length = len(tf[0][1])# get the length of documents
	for key, value in df:
		newidf = math.log10(float(tffile_length)/value)
		idf.update({key:newidf}) # update idf dict
	idf = [(v,k) for v,k in idf.items()] # change idf(dict type) to list of tuples
	# calculat the idf*tf value
	for k1,v1 in tf:
		for k2,v2 in idf:
			if k1==k2:
				newtfidf = [v2*num for num in v1]
				tfidf.update({k2:newtfidf}) # update tfidf dict
	tfidf = sorted([(k,v) for k,v in tfidf.items()])
	# # change the tfidt into list, remove the keys
	tfidf_lst = list()
	for k3,v3 in tfidf:
		tfidf_lst.append(v3)
	## save the tfidf: remove the key, and each list in represents a document vector
	tfidf_doc = list(map(list, zip(*tfidf_lst)))
	return tfidf_doc
	



"""
word_dic = utils.read_datastructure('word_dictonary.pkl')
df_dic = utils.read_datastructure('df_dictonary.pkl')
boolean_dic = utils.read_datastructure('boolean_dictonary.pkl')
tfidf_weight_calculation(word_dic,df_dic,boolean_dic,len(word_dic))
print('Done.')
"""

#print(len(word_dic['addit']))
#utils.writedic_to_csv(tf_list,'tf_test.csv')
#utils.readcsv('test.csv')

#correct
"""
df_file = utils.read_datastructure('df_dict.pkl')
tf_file = utils.read_datastructure('word_dict.pkl')
doc_tfidf_matrix = tf_idf_calculation(tf_file, df_file)
utils.store_datastructure('doc_tfidf_matrix.pkl',doc_tfidf_matrix)
"""
# doc_tfidf_distance = [math.sqrt(sum(val)) for val in doc_tfidf_matrix]
# utils.store_datastructure('doc_tfidf_distance.pkl',doc_tfidf_distance)
# doc_tfidf_normalize = []
# filelen = len(doc_tfidf_matrix)
# for i in xrange(0,filelen):
# 	v2 = doc_tfidf_distance[i]
# 	v1 = doc_tfidf_matrix[i]
# 	doc_tfidf_normalize.append([v1/v2 for v1 in doc_tfidf_matrix[i]])
# utils.store_datastructure('doc_tfidf_normalize.pkl',doc_tfidf_normalize)


# print(len(docTfidfMatrix[0])) # each list in docTfidfMatrix is 1*16287,
# 16287 is the number of terms
# print(docTfidfMatrix)










