'''
뒷 기능이 먼저 개발된다면 앞 기능 배포일에 같이 배포 

[7, 3, 6, 2, 1]
남은기간: 배포일 
7: 7
3: 7
6: 7
2: 7
1: 7

[5, 10, 1, 1, 20, 1]
5: 5
10: 10
1: 10
1: 10
20: 20
1: 20
'''
from collections import deque
def solution(progresses, speeds):
    answer = []
    stack = []
    work_days = deque()
    
    for i in range(len(progresses)):
        cur = progresses[i]
        work = (100 - cur) // speeds[i]  
        
        if (100 - cur) % speeds[i] != 0: 
            work_days.append(work+1)
        else:
            work_days.append(work)
            
    # cnt, top을 첫 기능에 맞춰서 초기화 
    cnt = 1
    top = work_days.popleft()
    
    while work_days:
        cur = work_days.popleft()
        
        # 앞 기능 배포 
        if cur > top: 
            answer.append(cnt)
            top = cur
            cnt = 0
            
        cnt += 1
            
    answer.append(cnt)
    return answer