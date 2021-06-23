while True:
  c,p = map(int, input().split())
  if c == p == 0:
    break
  print(c//p,c%p,"/",p)