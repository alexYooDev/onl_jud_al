def solution(s):
    p_num, y_num = 0, 0
    for i in range(0, len(s)) :
        if s[i]=='p' or s[i]=='P':
            p_num+=1
        elif s[i]=='y' or s[i]=='Y':
            y_num+=1
    return p_num==y_num

print(solution("pPoyY"))