#recursion

def solution(n):
    
    if n < 2:
        return n
    else:
        return (solution(n-1)+solution(n-2))

