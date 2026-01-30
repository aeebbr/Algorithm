# 기능 선후 방향은 큐와 같음: <- 선입선출 <- 
# 작업 완료일: 7, 3, 9
# front가 right보다 크거나 같다면, right는 front와 함께 나갈 수 있음 
import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    
    # 작업 완료일 
    done_days_q = deque()
    for p, s in zip(progresses, speeds):
        tmp = math.ceil((100 - p) / s)
        done_days_q.append(tmp)
    
    front = done_days_q.popleft()
    count = 1
        
    while done_days_q:
        cur = done_days_q.popleft()
        
        # front 배포 
        if cur > front:
            answer.append(count)
            front = cur 
            count = 1
            continue
        
        count += 1
    
    answer.append(count)
    
    return answer