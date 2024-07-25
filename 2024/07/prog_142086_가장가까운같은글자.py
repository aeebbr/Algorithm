def solution(s):
    answer = []
    dic = {}
    
    for i in range(len(s)):
        cur = s[i]
        if cur in dic:
            tmp = i - dic[cur]
            answer.append(tmp)
        else:
            answer.append(-1)
            
        dic[cur] = i
    
    return answer