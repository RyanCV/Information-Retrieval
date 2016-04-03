# Author: Yuanwei Wu
# Date: 3/16/2016, recove 3/22/2016, revised 4/3/2016
# Description: input: tf, df in list, 
# output: calculate idf= log10(N/df), only output tf*idf in list

import math
import utils

def tf_idf_calculation(tf, df):
	tfidf = dict()
	idf = dict()
	tffile_length = len(tf[0][1])# get the length of documents
	# print(tffile_length)
	# calculte the idf value
	for key, value in df:
		# print("key",key,"value",value)
		newidf = math.log10(float(tffile_length)/value)
		idf.update({key:newidf}) # update idf dict
	idf = [(v,k) for v,k in idf.items()] # change idf(dict type) to list of tuples
	# print("idf\n",idf)
	
	# calculat the idf*tf value
	for k1,v1 in tf:
		for k2,v2 in idf:
			if k1==k2:
				newtfidf = [v2*num for num in v1]
				tfidf.update({k2:newtfidf}) # update tfidf dict
	# change tfidf (dict) to list of tuples, and sorted based on the key,
	# therefore, the order in tfidf_doc has the same order with the terms order
	tfidf = sorted([(k,v) for k,v in tfidf.items()])
	# print("tfidf\n", tfidf)
	# # change the tfidt into list, remove the keys
	tfidf_lst = list()
	for k3,v3 in tfidf:
		tfidf_lst.append(v3)
	# return tfidf_lst
	# print("tfidf_lst\n", tfidf_lst)

	## save the tfidf: remove the key, and each list in represents a document vector
	tfidf_doc = list(map(list, zip(*tfidf_lst)))
	# print("tfidf_doc \n", tfidf_doc)
	return tfidf_doc


## test the idf_calculation(tf,df)
# df_file = utils.read_datastructure('df_dict.pkl')
# # print(df_file[0:5])
# tf_file = utils.read_datastructure('word_dict.pkl')
# # print(tf_file[0:5])
# doc_tfidf_matrix = tf_idf_calculation(tf_file,df_file)
# # print(doc_tfidf_matrix)
# # save the doc_tfidf_matrix results in list
# utils.store_datastructure('doc_tfidf_matrix.pkl',doc_tfidf_matrix)
## print the tfidf results 
# docTfidfMatrix = utils.read_datastructure('doc_tfidf_matrix.pkl')

# print(len(docTfidfMatrix[0])) # each list in docTfidfMatrix is 1*16287,
# 16287 is the number of terms
# print(docTfidfMatrix)








