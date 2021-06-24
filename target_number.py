from itertools import product

def solution(numbers, target):

    # 배열로부터 더하기와 빼기를 할 튜플이 담긴
    # 정수리스트를 만든다
    l = [(x, -x) for x in numbers]
    print(l)
    # 주어진 튜플로 서로 곱한 값을 리스트로 만듬
    s = list(map(sum, product(*l)))
    #모든 경우의 수 중 target에 이른 값만 세어 리턴
    return s.count(target)