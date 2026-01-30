# prices를 그래프라고 생각하면 쉬움 
# 탐색 방향: <- 역방향 <-
# prices의 인덱스를 같이 엮어서 튜플로 만들기 

# 가격이 떨어지는 최초의 시점 찾기. 정석대로 하면 초과됨. 비교군을 최대한 적게 만들기. => 역방향으로 해야만. 역방향으로 하면서 비교군을 최대한 줄여야 함. 
# 비교군에는 작은 것들이 있어야 함 
# 비교군이 나보다 크면, 해당 비교 원소는 제거. 그 뒤의 다음 비교 원소와 비교하기, 비교하기 반복. 
from collections import deque
def solution(prices):
    answer = deque()
    # 비교군 
    stack = []
    
    for i in range(len(prices)):
        prices[i] = ((prices[i], i))
    
    for i in range(len(prices)-1, -1, -1):
        cur, cur_idx = prices[i]
        drop_sec = len(prices) - i - 1 # 끝까지 가격이 떨어지지 않은 경우로 초기화 
            
        # 비교군과 비교하기 
        while stack:
            top, top_idx = stack[-1]
            
            # top이 더 크거나 같으면 top은 가치 없음. 스택에서 제거 
            if cur <= top:
                stack.pop()
            # top이 더 작으면 가격 떨어지는 순간 찾은 것
            else:
                drop_sec = top_idx - cur_idx
                break
        
        # 스택에 현재 원소 삽입 
        stack.append((cur, cur_idx))
        # 시간 기록 
        answer.appendleft(drop_sec)
            
    return list(answer)