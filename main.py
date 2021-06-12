def get_divisor(n):
  n = int(n)
  divisors = []

  for i in range(1, n+1):
    if(n%i == 0):
      divisors.append(i)
  return divisors

def solution(left, right):
    answer = 0
    lists = []
    arr = []
    for i in range(left, right+1):
      lists.append(i)

    for i in lists:
      arr.append(get_divisor(i))
    for list in arr:
      if len(list) % 2 == 0:
        answer += list[len(list)-1]
      else:
        answer -= list[len(list)-1]

    return answer
