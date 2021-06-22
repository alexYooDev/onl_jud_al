def solution(n):
    cnt = 0
    # 1부터 15까지 // 아래 중첩 반복문은 요소 전부탐색
    for i in range(1, n+1):
        # sum을 0으로 set
        sum = 0
        # 1부터 15까지
        for j in range(i, n+1):
            sum += j
            print(sum)
            if sum == n:
                cnt+=1
                break
                # 합이 n보다 큰 경우, 루프 종료
            elif sum > n:
                break
    return cnt