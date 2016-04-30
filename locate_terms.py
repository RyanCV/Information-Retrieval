#by Yang Tian
#calculate matched words in docs based on queries
import utils


def locate_sentence_with_indice(docstring,indice):
    mid_index = (indice[0]+indice[-1])/2
    if mid_index-50 >= 0:
        start = mid_index-50
    else:
        start = 0
    if mid_index+50 < len(docstring):
        end = mid_index+50
    else:
        end = len(docstring)-1   
    return docstring[start:(end+1)]

#parameters: 
#query_string_list: list of processed query words
#doc_ids: doc_ids need to be gone through
#return:
#words indice need to be highlighted
def locate_terms_indocs(query_string_list,doc_ids):
    print 'query list:'
    print query_string_list
    print 'docs ids:'
    print doc_ids
    proc_doc_list = utils.get_ir_preprocessed_docs_list()
    cand_doc_list = [proc_doc_list[i] for i in doc_ids]
    
    result_lists = []
    result_strpart_lists = []
    for doc_item in cand_doc_list:
        
        matches_list = []
        for query_item in query_string_list:
            occur = [i for i, x in enumerate(doc_item) if x == query_item]
            
            matches_list += occur
        matches_list.sort()
        matches_list = [x for x in matches_list if x-matches_list[0] < 100]
        str_part_list = locate_sentence_with_indice(doc_item,matches_list)
        #print 'str_part_list:'
        #print str_part_list
        result_lists.append(matches_list)
        result_strpart_lists.append(str_part_list)
        
    return result_lists,result_strpart_lists
        
    