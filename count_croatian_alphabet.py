cr_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in cr_al:
  word = word.replace(i, "c") 

print(len(word))