str = input()

chunks = [str[i:i+10] for i in range(0, len(str), 10)]

for i in chunks:
  print(i)