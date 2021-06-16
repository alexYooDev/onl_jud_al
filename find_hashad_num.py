def solution(x):
    
    h = sum(list(map(int, str(x))))
        
    return True if x%h == 0 else False