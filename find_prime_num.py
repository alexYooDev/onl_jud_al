def solution(n):

    cnt = 0

    # num = 2부터 n까지 2,3,4,5...n
    for num in range(2, n+1):
        # i = 2부터 num(2,3,4,5,..n)까지의 수
        for i in range(2,num):
            # num(2,3,4,5...) 이 i(2,3,4,5,...n)으로 나누어 떨어짐
            if num%i == 0:
                break
        else: 
            cnt+=1
            #효율성 실패
    return cnt