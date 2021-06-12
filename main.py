
def convert(num, base):
  T = "0123456789ABCDEF"
  q,r = divmod(num,base)
  if q == 0:
    return T[r]
  else:
    return convert(q,base)+T[r]

def div(word):
  return [char for char in word]

def solution(n):
    answer = 0
    stk = []
    three = []
    result = convert(n, 3)
    stk = div(str(result))
    for i in range(0,len(stk)):
        three += stk.pop()
    temp = ''.join(three)
    answer = int(temp, base=3)
    return answer