import collections

def solution(arr):
  answer = 0
  cnt = []
  for i in arr:
    if arr.count(i) >= 2:
      cnt.append(i)
  answer = list(collections.Counter(cnt).values())
  if len(cnt) == 0: answer = -1
  print(answer)
  return answer