#problem: input the number of students, then their scores to make a list that is descending sorted
#first input = number of students next input = their scores

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)