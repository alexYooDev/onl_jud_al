def solution(n):
    i = 1
    while i <= n:
        if n%i == 0:
            return i
        i += 1

print(solution(13))