# front와 나머지를 어떻게 비교? 
    # 나머지 중에서 max와 비교할까? => max 찾기 위해서 매번 전체 탐색하게 됨 
    # => 순위 오름차순으로 스택에 넣고, top만 꺼내서 비교하면 됨. 만약 top이 front여도 상관 없음. 
# [(우선순위, 타겟여부)]
from collections import deque
def solution(priorities, location):
    answer = 0
    stack = sorted(priorities)
    q = deque()
    
    for i in range(len(priorities)):
        if (i) == location:
            q.append((priorities[i], True))
        else:
            q.append((priorities[i], False))
            
    while q:
        front, isTarget = q.popleft()
        top = stack[-1]
        
        # 현재 프로세스 실행 
        if front == top:
            answer += 1
            stack.pop()
            if isTarget:
                break
        else:
            q.append((front, isTarget))

    return answer