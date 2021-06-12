def solution(arr1, arr2):
    answer = [[]]
    list2 = arr1.pop()
    list1 = arr1.pop()
    list4 = arr2.pop()
    list3 = arr2.pop()
    answer = [[x+y for x,y in zip(list1,list3)],[a+b for a,b in zip(list2,list4)]]
    return answer