def solution(num):
    if num != 1:
        for i in range(500):
            num = num/2 if num%2 == 0 else num*3+1        
            if num == 1:
                return i+1
    else: 
        return 0
    return -1