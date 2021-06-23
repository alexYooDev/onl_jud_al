line = []
white = ''

for i in range(8):
  line.append(input())

for i in line:
  if line.index(i)%2 == 0:
    white+=i[::2]
  else: white+=i[1::2]

print(white.count('F'))