# Author: Yuanwei Wu
# Date: 3/16/2016
# Description: calculate idf= log10(N/df), and tf*idf

# df, tf, idf are dictionary
# import math

# def idf_calculation(df):
# 	idf = dict()
# 	df_length = len(df)
# 	for key, value in df.items():
# 		print df
# 		idf[key] = math.log10(float(df_length)/df[key])
# 	return idf
	

# df = {'my':1, 'you':2, 'he':3}
# idftest = idf_calculation(df)
# print idftest
# print len(idftest)

# tf = {'my':[1,2,3], 'you':[4,5,6]}
# idf = {'my':2, 'you':3}
# b = a.update((key,value*2) for key, value in a.items())

# print a
# print a['my'][0]
# print len(a.items()[0])
# print [len(value) for key, value in a.items()]
# def tf_idf_calculation(tf, idf):
# 	weight = dict()
# 	for key, value in tf.items():
# 		vec = tf[key]
# 		idfvalue = idf[key]
# 		tf[key] = [num*idfvalue for num in vec]
# 		weight = tf
# 	return weight

# wei = tf_idf_calculation(tf,idf)
# print wei

import math
import utils

def idf_calculation(df):
	df_length = len(df[1])
	idf = list()
	idf.append(df[0])
	idf_elem = list()
	for elem in df[1]:
		newelem = math.log10(float(df_length)/elem)
		idf_elem.append(newelem)
	idf.append(idf_elem)
	return idf

# a = [['a'],[1,2,3,4]]
# b = idf_calculation(a)
# print b

# dftest = utils.read_datastructure('df_dict.pkl')
# print dftest
wordtest = utils.read_datastructure('word_dict.pkl')
# print wordtest
print type(wordtest)
# atest = idf_calculation(dftest)
# print atest

# def tf_idf_calculation(tf, idf):
# 	tf_length = len(tf[1])
# 	tf_idf = list()
# 	tf_idf.append(tf[0])
# 	tf_idf_elem = list()
# 	tf.update((x, map(x:x*2)) for x, y in tf[1])













