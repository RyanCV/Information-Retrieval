# Author: Yuanwei Wu
# Date: 3/16/2016, recove 3/22/2016
# Description: input: tf, df in list, 
# output: calculate idf= log10(N/df), only output tf*idf in list

import math
import utils

def tf_idf_calculation(tf, df):
	tfidf = dict()
	idf = dict()
	tffile_length = len(tf[0][1])# get the length of documents
	# calculte the idf value
	for key, value in df:
		newidf = math.log10(float(tffile_length)/value)
		idf.update({key:newidf}) # update idf dict
	idf = idf.items() # change idf to list of tuples
	
	# calculat the idf*tf value
	for k1,v1 in tf:
		for k2,v2 in idf:
			if k1==k2:
				newtfidf = list([v2*num for num in v1])
				tfidf.update({k2:newtfidf}) # update tfidf dict
	tfidf = tfidf.items() # change tfidf to list of tuples
	# change the tfidt into list, remove the keys
	tfidf_lst = list()
	for k3,v3 in tfidf:
		tfidf_lst.append(v3)
	return tfidf_lst

## test the idf_calculation(tf,df)
# df_file = utils.read_datastructure('df_dict.pkl')
# tf_file = utils.read_datastructure('word_dict.pkl')
# tfidf_dict = tf_idf_calculation(tf_file,df_file)
# tfidf_dict = sorted(tfidf_dict)
# # save the tfidf results in list
# utils.store_datastructure('tfidf_lst_dict.pkl',tfidf_dict)
## save the tfidf results in dictionary
# utils.store_datastructure('tfidf_dict.pkl',tfidf_dict)
## print the tfidf results 
# tfidfdict = utils.read_datastructure('tfidf_dict.pkl')
# print tfidfdict








