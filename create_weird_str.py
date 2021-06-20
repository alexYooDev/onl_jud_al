def solution(s):
    answer = ""
    s_split = s.split(" ")
    
    for j in range(len(s_split)):
        s_arr = list(s_split[j])
        
        for i in range(len(s_arr)):
            if i%2 == 0:
                s_arr[i] = s_arr[i].upper()
            elif i%2 == 1:
                s_arr[i] = s_arr[i].lower()
        s_split[j] = "".join(s_arr)
        
    answer = " ".join(s_split) 

    return answer