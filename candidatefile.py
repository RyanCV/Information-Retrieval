#choose candidate files based on query
#by Yang Tian
import utils
from utils import *


#use boolean model to choose candidate files based on query
#parameters:
#   query: list of words in the query
#   files_num: number of all documents
#return: list of file indice which contains at least one item in the query words
def candidate_files(query,files_num):
    #boolean_dic = utils.read_datastructure('boolean_dictonary.pkl')
    boolean_dic = get_ir_boolean_dictionary()
    parts_num = files_num/32
    if files_num%32 == 0:
        end = 32
    else:
        end = files_num%32
        parts_num += 1

    result_array = [0]*parts_num

    for word in query:
        if boolean_dic.has_key(word):
            current_array = boolean_dic[word]
            #print(word)
            #print(current_array)
            i = 0
            for x,y in zip(result_array,current_array):
                result_array[i] = result_array[i]|current_array[i]
                i+=1
    i = 0
    files_indice = []
    for value in result_array:
        if i < parts_num-1:
            count = 32
        else:
            count = end
        out = 0
        compare = 1<<(count-1)
        for j in range(0,count):
            out = compare & (value << j)
            if out != 0:
                files_indice.append(i*32+j)
        i+=1
    #print files_indice
    return files_indice


#a = ['zumwalt','zuni','zwinger']
#b = ['zuni','zwinger']
#c = ['ku','bast']
#candidate_files(c,91)
#candidate_files(b,91)