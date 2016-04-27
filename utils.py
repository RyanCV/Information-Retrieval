#Commonly used methods
#by Yang Tian
import pickle
import csv






def store_datastructure(path,data):
    with open(path, 'wb') as f:
        pickle.dump(data, f, -1)

def read_datastructure(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def writedic_to_csv(dic_list,csv_filename):
    writer = csv.writer(open(csv_filename,'wb'))
    for item in dic_list:
        writer.writerow(item)

def readcsv(csv_filename):
    reader = csv.reader(open(csv_filename,'rb'))
    for item in reader:
        print item

def init_all_data():
    global ir_file_path_list
    global ir_df_dictionary
    global ir_boolean_dictionary
    global ir_tfidf_matrix
    global ir_doc_number
    ir_doc_number = 492
    ir_file_path_list = read_datastructure('filepath_list.pkl')
    ir_df_dictionary = read_datastructure('df_dictonary.pkl')
    ir_boolean_dictionary = read_datastructure('boolean_dictonary.pkl')
    ir_tfidf_matrix = read_datastructure('doc_tfidf_matrix.pkl')

def get_ir_doc_number():
    return ir_doc_number

def get_ir_df_dictionary():
    return ir_df_dictionary

def get_ir_boolean_dictionary():
    return ir_boolean_dictionary

def get_ir_tfidf_matrix():
    return ir_tfidf_matrix

def get_ir_file_path_list():
    return ir_file_path_list
