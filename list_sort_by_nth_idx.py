def solution(strings, n):

    #정렬을 한 string 리스트를 key(x = strings의 요소 x[n]번째)를 기준으로 정렬
    sorted(sorted(strings), key = lambda x: x[n])