from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 1초에 1length 지날 수 있음 
    # 트럭 순서는 고정임 
    # 다리는 일차선이기 때문에 동시에 두 트럭이 나란히 진입할 수 없음 
    
    gridge_q = deque() # 다리에 올라가 있는 트럭 
    gridge_q.append((0, bridge_length))
    truck_q = deque(truck_weights) # 다리에 아직 올라가지 않은 트럭 
    total_weight = 0 # 다리에 있는 트럭의 무게 총합 
    
    while gridge_q:
        # 맨 앞 트럭이 다리를 다 지났는지 확인 
        fw, ft = gridge_q.popleft()
        if ft != bridge_length:
            gridge_q.appendleft((fw, ft))
        else:
            total_weight -= fw
            
        # 다리에 새 트럭 올리기 
        if truck_q:
            cur = truck_q.popleft()
            
            # 길이, 무게 조건이 맞으면 새 트럭 올리기 
            if len(gridge_q) < bridge_length and cur <= weight - total_weight:
                gridge_q.append((cur, 0)) # (무게, 시간)
                total_weight += cur 
            else:
                truck_q.appendleft(cur)

        # 다리 위 모든 트럭에 시간 증가 
        for _ in range(len(gridge_q)):
            w, t = gridge_q.popleft()
            gridge_q.append((w, t+1))
            
        answer += 1
        # 1초 경과 완료 
        
    return answer