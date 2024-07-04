def solution(s):
    answer = 1
    
    x = s[0]
    x_cnt = 1
    other_cnt = 0
    
    for i in range(1, len(s)):
        if x_cnt == other_cnt:
            answer += 1
            if i != len(s)-1:
                x = s[i]
                x_cnt = 1
                other_cnt = 0
                continue
                
        cur = s[i]
        if cur != x:
            other_cnt += 1
        else:
            x_cnt += 1
            
    return answer