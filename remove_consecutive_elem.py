from itertools import groupby

def solution(arr): 
    
    return [i[0] for i in groupby(arr)]