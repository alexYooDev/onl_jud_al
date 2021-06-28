def solution(n, computers):
    
    # n의 범위만큼 False가 할당된 배열 생성
    connected = [False for i in range(n)]
    # 0으로 초기화
    answer = 0
    
    # 처음 방문 노드(v) 의 범위 0~n-1
    for v in range(n):
        # 처음 노드가 방문되지 않았다면
        if connected[v] == False:
            #  재귀함수 dfs에 v를 넣음
            dfs(n, computers, v, connected)
            # 네트워크의 개수를 1 증가
            answer += 1
    return answer

# 깊이 우선 탐색을 할 함수 생성
def dfs(n, computers, v, connected):
    # 첫번째 노드가 방문되었다면
    connected[v] = True
    # 0~n-1 까지 범위의 c
    for c in range(n):
        # c가 v와 다르고 배열의 c번째 배열의 v요소가 1이면
        if c != v and computers[c][v] == 1:
            #c가 방문되지 않았다면
            if connected[c] == False:
                #c를 넣은 재귀함수 호출
                dfs(n, computers, c, connected)
            