'''
95 -> <1일 후> 99 -> <2일 후> 100 (이 날 끝에 배포)
93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99 -> <7일 후> 100 (이 날 끝에 배포)
'''
from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    done_day = deque() # 개발 완료일 
    
    for i in range(len(progresses)):
        # 100 - 93 = 7, 7 / 1 = 7
        # 100 - 30 = 70, 70 / 30 = 2.x -올림-> 3
        p = progresses[i]
        done_day.append(math.ceil((100 - p) / speeds[i]))

    cur = 0
    front = done_day.popleft()
    cnt = 1
    
    while done_day:
        cur = done_day.popleft()

        if cur > front:
            # 이전까지의 기능들 배포 
            answer.append(cnt)
            cnt = 0
            front = cur
            
        cnt += 1
        
    answer.append(cnt)

    return answer