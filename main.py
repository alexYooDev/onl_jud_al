
def search_median (arr):
    
    answer = 0
    arr.sort()
    length = len(arr)-1

    x = arr[int(length/2)]
    y = arr[int(length/2)+1]

    if length % 2 == 0:  
      answer = x
      
    else:   
      answer = (x+y)/2
      
    return answer
  
search_median([1,4,20,6,20,47,2,11,30,7,8,10,26])