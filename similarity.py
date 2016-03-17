#document similarity
#by Yang Tian and Xi Chen
import math

def vectorlength(vec):
    length = float(0)
    for num in vec:
        length += num*num
    return math.sqrt(length)

def simDistance(w1,w2):
    sim = float(0)
    for wi1, wi2 in zip(w1, w2):
        sim += wi1*wi2
    sim = sim/(vectorlength(w1)*vectorlength(w2))
    return sim

def computerSimilarity(query, listOfVectors):
    indexList= []
    if not listOfVectors:
        print query + "did not match any documents."
        return indexList

    if listOfVectors:
        for vector in listOfVectors:
            value = simDistance(query,vector)
            indexList.append(value)
        indexList.sort()
        return indexList
"""
query = [1,2,3,0]
listOfVectors = [[1,0,0,0],[1,3,1,1]]

output = computerSimilarity(query, listOfVectors)
print output
"""