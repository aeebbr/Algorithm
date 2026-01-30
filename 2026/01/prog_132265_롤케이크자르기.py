# 왼쪽, 오른쪽 덱 각각 둬서 원소 이동
from collections import deque, Counter
def solution(topping):
    answer = 0
    
    left, right = deque([topping[0]]), deque(topping[1:])
    l_cnt, r_cnt = Counter(left), Counter(right)
    
    while len(right) > 0:
        if len(l_cnt) == len(r_cnt):
            answer += 1
        
        r = right.popleft()
        left.append(r)
        
        r_cnt[r] -= 1
        if r_cnt[r] == 0:
            del r_cnt[r]
        
        if r in l_cnt:
            l_cnt[r] += 1
        else:
            l_cnt[r] = 1
            
    return answer