# 현재 idx부터 idx+9까지 범위 중에 want가 모두 포함되는지 확인 
from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_number = Counter({w:n for w, n in zip(want, number)})
    
    # 처음 열흘 확인 
    cur = Counter(discount[:10])
    if want_number == cur:
         answer += 1
            
    for i in range(len(discount)-10):
        cur[discount[i]] -= 1 # 줄어드는 제품 
        cur[discount[i+10]] += 1 # 늘어나는 제품 
        
        # 개수가 0이 되면 해당 항목 제거 
        if cur[discount[i]] == 0:
            del cur[discount[i]]
            
        if want_number == cur:
            answer += 1
    
    return answer