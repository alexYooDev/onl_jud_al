num = list(map(int, input().split()))

d = {1:"c", 2:"d", 3:"e", 4:"f", 5:"g", 6:"a", 7:"b", 8:"C"}

asc = sorted(d, )
dsc = sorted(d, reverse=True)

if num == asc:
  print('ascending')

elif num == dsc:
  print('descending')

else: print('mixed')