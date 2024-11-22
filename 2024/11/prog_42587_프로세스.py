'''
a, [b, c, d, a]
b, [c, d, a, b]
c, [d, a, b] ***
d, [a, b] ***
a, [b] ***
b ***
'''
from collections import deque
def solution(priorities, location):
    answer = 0 
    is_target_arr = [False] * len(priorities)
    is_target_arr[location] = True
    q = deque(list(zip(priorities, is_target_arr))) # 메인 큐, (우선순위, 타겟여부)
    sort_priorities = deque(sorted(priorities, reverse=True)) # 우선순위가 내림차순으로 들어있는 큐
    
    while q:
        front, is_target = q.popleft()
        first = sort_priorities.popleft() # 남은 것 중 가장 높은 우선 순위
        
        if front < first: # 실행 안 함 
            q.append((front, is_target))
            sort_priorities.appendleft(first)
        else: # 실행 함 
            answer += 1 
            
            # 타겟이라면 
            if is_target:
                break

    return answer