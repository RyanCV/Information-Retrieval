# Author: Yuanwei Wu & Yang Tian
# Date: 4/3/2016 4/22/2016
# Description: input: query, df and tf in list (use tf to find the number of documents), 
# output: query vector, it will be used to calculate the similarity of (Q,D)

import math
import utils

def tfidf_Query(query,df):
    vector_length = len(df)
    query_tf = dict.fromkeys(df, 0)
    for word in query:
        if df.has_key(word):
            query_tf[word] = query_tf[word]+1
    for word in df:
        query_tf[word] = query_tf[word]*math.log10(float(vector_length)/df[word])

    query_tf = sorted(query_tf.items())
    query_tf = [x[1] for x in query_tf]
    normlen = math.sqrt(sum(x*x for x in query_tf))
    query_tf = [x/normlen for x in query_tf]
    return query_tf


def tfidf_for_Query(query, df, tf):
	query_vector = dict()
	query_tf = dict()
	idf = dict()
	tffile_length = len(tf[0][1])# get the length of documents
	# print(tffile_length)
	## calculte the idf value
	for key, value in df:
		# print("key",key,"value",value)
		newidf = math.log10(float(tffile_length)/value)
		idf.update({key:newidf}) # update idf dict
	idf = [(v,k) for v,k in idf.items()] # change idf(dict type) to list of tuples
	# print("idf\n",idf)
	
	## calculat the tf value for the query vector with same dimension of doc.
	for key, value in df:
		for word in query:
			if word == key:
				query_tf.update({key:1})
			else:
				query_tf.update({key:0})
	query_tf = [(v,k) for v,k in query_tf.items()]
	# return query
	# print("query_tf\n",query_tf)

	## calculate the query vector (tfidf)
	for k1,v1 in idf:
		for k2,v2 in query_tf:
			if k1==k2:
				newtfidf = v1 * v2
				query_vector.update({k2:newtfidf}) 
	## sorted the vector, therefore it corresponding to the terms order(alphabetic)				
	query_vector = sorted([(v,k) for v,k in query_vector.items()])
	# print("query_vector\n", query_vector)
	# # remove the key, and each list in represents a query vector
	query_vector_lst = list()
	for k3,v3 in query_vector:
		query_vector_lst.append(v3)
	# print("query_vector_lst\n", query_vector_lst)
	return query_vector_lst
	



#df_file = utils.read_datastructure('df_dictonary.pkl')
#c = ['ku','bast']
#tfidf_Query(c,df_file)






