def solution(strings, n):
    answer = []
    
    for i in range(len(strings)):
        s = strings[i]
        strings[i] = (s, s[n])
        
    strings = sorted(strings, key = lambda x: (x[1], x[0]))
    
    for a, b in strings:
        answer.append(a)
    
    return answer