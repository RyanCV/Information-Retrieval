#Construct Inverted Index and get frequency information
#by Yang Tian
import string
import os
import os.path
import collections
import utils

path = 'RemovedString/'
num_files = len([f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))])-1
init_boolean = [0]*num_files

#print(init_boolean)
word_dict = {}
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
        else:
            current_value = [0]*num_files
            current_value[filecount] += 1
            word_dict[word] = current_value
    filecount+=1
word_dict = collections.OrderedDict(sorted(word_dict.items()))
#print(word_dict)
dic_len = len(word_dict)
df_dict = {}
for key, value in word_dict.iteritems():
    df_dict[key] = 0
    for freq in value:
        if freq > 0:
            df_dict[key]+=1

word_dict = collections.OrderedDict(sorted(word_dict.items()))
df_dict = collections.OrderedDict(sorted(df_dict.items()))
#print(word_dict)
#print(df_dict)
utils.store_datastructure('word_dict.pkl',word_dict)
utils.store_datastructure('df_dict.pkl',df_dict)

print("Done.")



