from collections import Counter

def count_duplicates(arr):
  cnt = []
  for i in arr:
    if arr.count(i) >= 2:
      cnt.append(i)
  if not cnt:
    return [-1]
  return list(Counter(cnt).values())

print(count_duplicates([1,2,3,3,3,3,4,4]))