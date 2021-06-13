
def solution(arr):
    
    answer = 0
    arr.sort()
    length = len(arr)-1
    
    x = int(length/2)+1
    print(arr)

    if length % 2 == 0:  

      answer = x
    else:   
      answer = (x+(x+1))/2
    
    return answer

print(solution([1,4,5,6, 47 ,2,3,11,30,7,8,9]))