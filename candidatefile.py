#choose candidate files based on query
#by Yang Tian
import uitls

def binary_and(x,y):
    if x == 0 and y == 0:
        return 0
    else:
        return 1

def candidate_files(query,term_dict,files_num):
    result_array = [0]*files_num
    i = 0
    for word in query:
        if term_dict.haskey(word):
            current_array = term_dict[word]
            for x,y in zip(result_array,current_array):
                result_array[i] = binary_and(x,y)
                i+=1
    i = 0
    for value in result_array:
        if value == 1:
            print(i)
            i+=1

a = ['addit', 'text','zwinger','zwinger']
t_dic = utils.read_datastructure('word_dictonary.pkl')
candidate_files(a,t_dic,)