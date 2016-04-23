# Author: Yuanwei Wu
# Date: 3/16/2016, recove 3/22/2016, revised 4/3/2016, update normalize: 4/23/2016
# Description: input: tf, df in list, 
# output: calculate idf= log10(N/df), only output tf*idf in list

import math
import utils

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
	




# df_file = utils.read_datastructure('df_dict.pkl')
# tf_file = utils.read_datastructure('word_dict.pkl')
# doc_tfidf_matrix = tf_idf_calculation(tf_file, df_file)
# utils.store_datastructure('doc_tfidf_matrix.pkl',doc_tfidf_matrix)
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










