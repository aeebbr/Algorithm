# 탐색 방향: <- 역방향 <-
# 덱에 후보군 넣기. 후보군은 오름차순꼴이어야 함. 중간에 작은 원소가 있으면 안됨.
# 뒤에서부터 탐색하면서, 원소가 front 보다 작다면 front가 적합
    # front보다 크다면 front는 삭제, 그 다음 front 비교  
from collections import deque
def solution(numbers):
    answer = deque()
    q = deque()
    
    while numbers:
        cur = numbers.pop()
        
        while True:
            if not q:
                answer.appendleft(-1)
                break
            else:
                front = q[0]
                # 찾음 
                if cur < front:
                    answer.appendleft(front)
                    break
                else:
                    q.popleft()
        q.appendleft(cur)
        
    return list(answer)