import time
start_time = time.time() #start counting time
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

end_time = time.time() #end counting time

print("time:", end_time - start_time) #print the time taken