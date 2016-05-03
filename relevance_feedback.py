### Relevance feedback for EECS 767 Information retrieval
### Author: Xi Chen

### input three elements: 1. the original query. 2. the vectors of relevant docs. 3. the vectors of irrelevant docs.
### output the new query vector got by using Rocchio
### input the new query vector and candidare docs and then use the new query to re-do similarity + proximity
### output a ranked list of docs indices

import numpy as np



def newQuery(query, relevant_doc, irrelevant_doc):
    ## set a, b and c
    a = 0.5
    b = 0.5
    c = -0.1
    
    q0 = np.array(query)
    relevantD = np.array(relevant_doc)
    irrelevantD = np. array(irrelevant_doc)
    
    releNum = float(len(relevantD))
    irreleNum = float(len(irrelevantD))
    
    totalReleVec = sum(relevantD)

    
    totalIrreleVec = sum(irrelevantD)
    
    if releNum ==0:
        if irreleNum !=0:
            newQ = a*q0  + c*totalIrreleVec/irreleNum
            return newQ.tolist()
        else:
            newQ = q0
            return newQ.tolist()
            
    if irreleNum ==0:
        newQ = a*q0 + b*totalReleVec/releNum
        return newQ.tolist()
    
    else:
        newQ = a*q0 + b*totalReleVec/releNum + c*totalIrreleVec/irreleNum
    
    return newQ.tolist()
    
""""
query =[0, 0.5, 1.2]
rele = [[0.2, 0.3,0.8],[0.1, 0.2, 0.0]]
irele = [[0.9, 0.1, 0.1], [0.1, 0.1, 0.1], [0,0,0]]
print newQuery(query, rele, irele)

"""