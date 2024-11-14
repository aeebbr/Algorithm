def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for t in tangerine: 
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
            
    cnt_list = sorted(list(dic.values()), reverse=True)
    
    for c in cnt_list:
        if k <= 0:
            break 
        
        answer += 1
        k -= c
    
    return answer