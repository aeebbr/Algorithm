def solution(strings, n):
    answer = []
    s = []
    
    for i in strings:
        s.append(i[n])
        
    tmp = list(zip(s, strings))
    
    for t in tmp:
        answer.append(t[1])
    
    
    return answer