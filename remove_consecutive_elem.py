def solution(arr): 
    
    prev_elem = None
    new_list = []
    for elem in arr:
        if elem != prev_elem:
            new_list.append(elem)
            prev_elem = elem
 
    return new_list