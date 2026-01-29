# want 원소가 모두 포함돼야 함 
# 투 포인터 
from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    left, right = 0, 9
    count = dict(Counter(discount[:9]))
    
    while right < len(discount): 
        if discount[right] in count:
            count[discount[right]] += 1 
        else:
            count[discount[right]] = 1 
        
        # 항목 비교 
        flag = True
        for i in range(len(want)):
            w = want[i]
            n = number[i]
            
            if w in count and n <= count[w]:
                continue
            
            # 실패 
            flag = False
            break
            
        if flag:
            answer += 1
            
        count[discount[left]] -= 1 
        
        left += 1
        right += 1
        
    return answer