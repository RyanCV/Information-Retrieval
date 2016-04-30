## Author: Xi Chen
## input a dict including path and site  and another list including only path.
## Output the path related sites
from utils import read_datastructure 
from utils import store_datastructure

dic = read_datastructure('finalFeedList.pkl')
path_list = read_datastructure('filepath_list.pkl')


for n, i in enumerate(path_list):
    path_list[n] = i.split("/")[-1]
    
#print path_list

path_value_list = []

for i in path_list:
    path_value_list.append(dic.get(i))
    
#print path_value_list[0:10]
store_datastructure('path_value_list.pkl', path_value_list)