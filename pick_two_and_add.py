
from itertools import combinations

def solution(numbers):
    answer = []
    temp = []
    cmb = list(set(combinations(numbers, 2)))
    for cb in cmb:
        temp += [sum(cb)]
        answer = list(set(temp))
        answer.sort()
               
    return answer

print(solution([2,1,3,4,1]))