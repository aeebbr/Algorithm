def solution(t, p):
    answer = 0
    
    for i in range(0, len(t)-len(p)+1):
        num = ''
        for j in range(len(p)):
            num += t[i+j]
            
        if int(num) <= int(p):
            answer += 1
    return answer