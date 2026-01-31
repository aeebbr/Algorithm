'''
1회 동작: 삭제 -> 삽입 

합이 큰 쪽이 작은 쪽으로 숫자 넘기기 반복 
어차피 옮길 수 있는 숫자는 각 큐의 front 밖에 없음 => front 비교해서 옮기기 
'''
from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    total1 = sum(q1)
    total2 = sum(q2)
    
    # 서로 모든 원소를 주고 받으면 limit번이 됨   
    limit = (len(q1) * 2) * 2
        
    if (total1 + total2) % 2 != 0:
        return -1
    
    while q1 and q2:
        # 서로 모든 원소를 주고 받아서 원점으로 돌아오면 실패 
        if answer == limit:
            return -1
        
        # total2 -> total1 옮기기 
        if total1 < total2:
            front2 = q2.popleft()
            q1.append(front2)
            total1 += front2
            total2 -= front2
            answer += 1
        # total1 -> total2 옮기기 
        elif total1 > total2:
            front1 = q1.popleft()
            q2.append(front1)
            total2 += front1
            total1 -= front1
            answer += 1
        else:
            return answer

    return -1