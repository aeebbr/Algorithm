from collections import deque

def solution(menu, order, k):
    answer = 0
    
    # 남은 입장 시간 
    enter = deque([x * k for x in range(len(order))])
    # 현재 입장한 모든 입장 시간
    q = deque([enter.popleft()])
    
    # 현재 손님의 나가는 시간 
    cur = 0
    
    # 주문 순회 
    for i in range(len(order)):
        # 나가는 시간 
        # 이전 손님 나가는 시간이 내 입장 시간보다 더 후라면, 이전 손님 나간 시간부터 내 거 제조 
        cur = max(cur, i*k) + menu[order[i]]
        
        # 현재 손님 나가기 전에 다음 입장 한다면
        while enter and enter[0] < cur:
            # 다음 손님 들어오기 
            q.append(enter.popleft())
            
        # 최대 입장수 갱신 
        answer = max(answer, len(q))
        # 현재 입장한 손님 나가기 
        q.popleft()
        
        # 현재 손님 나가는 시간과 다음 입장이 겹친다면 
        # 위 로직에서 현재 손님 나갔으니 그 후에 다음 입장하는 것 
        if enter and enter[0] == cur:
            # 다음 손님 들어오기 
            q.append(enter.popleft())
    
    return answer