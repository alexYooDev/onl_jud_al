def solution(brown, yellow):
    #카펫 전체 크기
    total = brown+yellow
    # 가로 길이 구함 (가로길이부터 2가 될때까지 -1)
    for h in range(total,2,-1):
        #전체 가로길이로 나누어떨어지면
        if total%h == 0:
            #세로는 전체를 가로로 나눈 몫
            v = total//h
            #노란색 칸의 가로 세로는 전체의 가로 세로 보다 2칸 없기 때문에 체크
            if yellow == (h-2)*(v-2):
                #전체의 가로 세로 
                return [h,v]