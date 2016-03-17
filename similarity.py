#document similarity
#by Yang Tian
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