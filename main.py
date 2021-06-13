import re

def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True

    if re.findall('[a-z]+', s):
        answer = False
    
    return answer
print(solution("123456"))