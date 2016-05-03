### Author  Xi Chen
### 1. read source files(after preprocess)
### 2. calculate minWindow for each file in the reading
### 3. return a list of minWindow values 
### 4. normalize the value
import numpy as np
import copy
import os
import utils
from similarity import vectorlength
from similarity import simDistance


def readfiles(dicName):
    
    AllFiles =[]
    
    for filename in os.listdir(dicName):
        #print filename
        preprocessed_file = open(dicName+"/"+filename, 'r')
        
        document = preprocessed_file.read().split()
        #print type(document)
        
        AllFiles.append(document)
        preprocessed_file.close()
        
    #utils.store_datastructure('preprocessed_docs_list.pkl',AllFiles)
    return AllFiles
        
        
        
#readfiles("Removed")

#docs = utils.read_datastructure('preprocessed_docs_list.pkl')




def smallestWindow(query, document):
    begin =0
    size = 100000
    start =0
    Length = len(query)
    #docLength = len(document)
    mark1={};
    
    for term in query:
        if term not in mark1:
            mark1[term] =1
        else: mark1[term] +=1
    
    mark2 = copy.deepcopy(mark1)
    
    for n,i in enumerate(document):
        if (document[n] in mark2) and (mark2[document[n]]>0):
            mark1[document[n]] -=1
            if mark1[document[n]] >=0:
                Length-=1
                
            if Length ==0:
                while True:
                    if (document[begin] in mark2) and (mark2[document[begin]]>0):
                        if mark1[document[begin]] < 0:
                            mark1[document[begin]] +=1
                        else:
                            break
                    begin +=1
                        
                if size>n-begin+1:
                    size = n-start+1
                    start = begin
        
    return len(document[start:start+size])
        
        
#print smallestWindow(["A","B"],["A","B","C","D"])

#input RankedList from similarity result and query list
#output a new ranked list by both similarity and term proximity results. 
#output[0] is ranked docs indices. output[1] is ranked value        
def newRankedList(docs, RankedDocList, query):
    
    output =[]
    newDocIndices = []
    
    rankedIndice = RankedDocList[0]
    rankedSimiValue = RankedDocList[1]
    
    term_proximity=[]
    for i in rankedIndice:
        
        if len(docs[i]) == smallestWindow(query,docs[i]):
            term_proximity.append(1000000)
        else:
            term_proximity.append(smallestWindow(query, docs[i]))
        
    #normalization
    #maxLength= float(max(term_proximity))
    
    term_proximity = [1/float(x) for x in term_proximity]
    
    ## set  a and b
    a = 0.5
    b = 0.5
    
    newSim = np.array(rankedSimiValue)*a
    newProximity = np.array(term_proximity)*b
    
    simAndProxi =[x+y for x,y in zip(newSim, newProximity)]
    
    rankedIndices = sorted(range(len(simAndProxi)), key = lambda k: simAndProxi[k])
    
    for i in rankedIndices:
        newDocIndices.append(rankedIndice[i])
    
    newDocIndices.reverse()
    simAndProxi.sort()
    simAndProxi.reverse()
    
    output.append(newDocIndices)
    output.append(simAndProxi)
    
    return output
    
""""        
rlist =[[4,1,3],[0.4, 0.1, 0.05]]
q =['nation', 'park']
result = newRankedList(docs, rlist, q)
print result
"""    
    

























    
        
    