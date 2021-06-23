from math import sqrt

def solution(n):
    
    # 3,5,7의 집합 자료형을 만든다
    num = set(range(3,n+1,2))
    # 3부터 n의 제곱근 + 2 (루트10 = 3 에 +2 = 5)까지의 수 i
    for i in range(3, int(sqrt(n))+2):
        # i가 num에 있다면
        if i in num:
            num -= set(range(2*i, n+1, i))
            print(set(range(2*i, n+1, i)))
    return len(num)+1