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