'''
<조건>
- 트럭은 1초에 다리 길이 1씩 전진함 
- 트럭은 올라갈 수 있으면 1초에 한 대씩 다리에 올라갈 수 있음 
- 다리 길이는 bridge_length임 

case 1
- 다리 길이 = 다리에 올라갈 수 있는 최대 대수 = 한 대가 지나야 하는 칸 수 = 2 
1. 다리 위: -, front: 7, pop, 다리 위: (7, 1)
2. 다리 위: 7, front: 4, 최대 무게 초과하므로 pop하지 않음, 다리 위: (7, 2)
3. 다리 위: -, front: 4, pop, 다리 위: (4, 1)
4. 다리 위: (4, 1), front: 5, pop, 다리 위: (4, 2), (5, 1)
5. 다리 위: (5, 1), front: 6, 무게 초과, 다리 위: (5, 2)
6. 다리 위: -, front: 6, pop, 다리 위: (6, 1)
7. 다리 위: (6, 1), 다리 위: (6, 2)
8. 트럭 이동 완료 
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    def update_truck(total_weight):
        # 다리 위 트럭 시간 갱신: 1초씩 증가 
        for _ in range(len(bridge_q)):
            truck, time = bridge_q.popleft()
            
            # 트럭 제거 
            if time + 1 == bridge_length:
                total_weight -= truck
            else:
                bridge_q.append((truck, time+1))
    
        return total_weight
    
    answer = 1
    total_weight = 0 # 다리 위에 있는 무게 총합 
    wait_q = deque(truck_weights) # 대기 트럭 
    bridge_q = deque() # 다리 위 트럭 
    limit_weight = weight # 변수 이름 변경 
    
    # 대기 큐와 다리 큐 모두에 트럭이 없으면 종료 
    while wait_q:
        front = wait_q.popleft()
        
        # 최대 무게를 초과한다면 다리로 올리지 않음 
        if total_weight + front > limit_weight:
            wait_q.appendleft(front)
        else:
            # 다리 위로 올림  
            bridge_q.append((front, 0))
            total_weight += front
        
        # 다리 위 트럭 시간 갱신(1초씩 증가) 및 트럭 제거
        total_weight = update_truck(total_weight)
        answer += 1
        
    # 다리 큐 남아있다면 다리 위 남은 트럭 처리 
    while bridge_q:
        total_weight = update_truck(total_weight)
        answer += 1
    
    return answer