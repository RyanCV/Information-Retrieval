#Commonly used methods
#by Yang Tian
import pickle

def store_datastructure(path,data):
    with open(path, 'wb') as f:
        pickle.dump(data, f, -1)

def read_datastructure(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data