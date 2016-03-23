#Construct Inverted Index and get frequency information
#by Yang Tian
import string
import os
import os.path
import collections
import utils

#get tf information of query
#querylist should be a list of string
#return a term-tf list
def tf_of_query(querylist):
    w_dict = utils.read_datastructure('df_dict.pkl')
    dicsize = len(w_dict)
    query_dict = dict()
    for term,value in w_dict:
        query_dict[term] = 0
    for word in querylist:
        if query_dict.has_key(word):
            query_dict[word] += 1
    return sorted(query_dict.items())





#build Inverted Index from path and boolean model
def construct_inverted_index(path):
    num_files = len([f for f in os.listdir(path)
                     if os.path.isfile(os.path.join(path, f))])-1
    init_boolean = [0]*num_files

    #print(init_boolean)
    word_dict = {}
    boolean_dict = {}
    filecount = 0

    for filename in os.listdir(path):
        #print(filecount)
        if filename == '.DS_Store':
            continue
        readfile = open(path+filename,'r')
        readstring = readfile.read().split()
        readfile.close()
        for word in readstring:
            if word_dict.has_key(word):
                current_value = word_dict[word]
                current_value[filecount] += 1
                word_dict[word] = current_value
            
                boolean_value = boolean_dict[word]
                boolean_value[filecount] = 1
                boolean_dict[word] = boolean_value
            else:
                current_value = [0]*num_files
                current_value[filecount] += 1
                word_dict[word] = current_value

                boolean_value = [0]*num_files
                boolean_value[filecount] = 1
                boolean_dict[word] = boolean_value
        filecount+=1
    #word_dict = collections.OrderedDict(sorted(word_dict.items()))
    #print(word_dict)
    #print(sorted(boolean_dict.items()))

    dic_len = len(word_dict)
    df_dict = {}
    for key, value in word_dict.iteritems():
        df_dict[key] = 0
        for freq in value:
            if freq > 0:
                df_dict[key]+=1

    num_parts = num_files/32
    if num_files%32 != 0:
        num_parts+=1
    #return
    final_boolean_dict = {}
    for term,value in boolean_dict.iteritems():
        final_boolean_dict[term] = [0]*num_parts
        for i in range(0,num_parts):
            end = (i+1)*32
            if end > num_files: end = num_files
            part = value[i*32:end]
            out = 0
            for bit in part:
                out = (out << 1) | bit
            final_boolean_dict[term][i] = out
    
    #print(sorted(final_boolean_dict.items()))
    utils.store_datastructure('boolean_dictonary.pkl',collections.OrderedDict(sorted(final_boolean_dict.items())))
    utils.store_datastructure('word_dictonary.pkl',collections.OrderedDict(sorted(word_dict.items())))
    utils.store_datastructure('df_dictonary.pkl',collections.OrderedDict(sorted(df_dict.items())))
    word_dict = sorted(word_dict.items())
    final_boolean_dict = sorted(final_boolean_dict.items())
    #print(final_boolean_dict)
    df_dict = sorted(df_dict.items())
    utils.store_datastructure('word_dict.pkl',word_dict)
    utils.store_datastructure('df_dict.pkl',df_dict)
    utils.store_datastructure('boolean_dict.pkl',final_boolean_dict)



#construct_inverted_index('RemovedString/')
#a = ['addit', 'text','zwinger','zwinger']
#t_dict = tf_of_query(a)
#for key, value in t_dict:
#    print(key,value)
#print("Done.")



