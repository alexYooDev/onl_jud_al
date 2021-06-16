from itertools import combinations

def isPrime(a,b,c):
    sum = a+b+c
    for i in range(2,sum):
        if sum%i == 0: return False
    return True

def solution (nums):
    answer = 0
    cmb = list(combinations(nums, 3))
    for i in cmb:
        if isPrime(i[0],i[1],i[2]):
            answer += 1
    return answer