'''
80, 70, 50, 50
=> 80/50 => 실패, 80만
70, 50, 50
=> 70/50 => 실패, 70만
50, 50
=> 50/50 => 성공
총 3개 
'''
from collections import deque
def solution(people, limit):
    answer = 0
    
    q = deque()
    people.sort(reverse=True)
    for p in people:
        q.append(p)
            
    while len(q) >= 2:
        max = q.popleft()
        min = q.pop()

        # 승선 끝 
        if (max + min) > limit:
            # 뺐던 min 도로 넣기 
            q.append(min)

        answer += 1
            
    if len(q) > 0:
        answer += 1
    
    return answer