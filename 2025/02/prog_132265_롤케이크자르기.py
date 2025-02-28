'''
*** 가짓수만 같으면 됨 

1. 모든 나눌 수 있는 범위대로 나누고, 매번 양쪽의 가짓수 따지기??? -> 토핑이 최대 백만개인데 효율 괜찮을까??? 
2. 다른 방법은?: 
    - 토핑을 두 덩어리로 나누기: 두 개의 리스트를 두어서 매번 새로운 범위를 설정해 slice 하지 말고, 왼쪽 큐와 오른쪽 큐를 나눠서 삽입 삭제하자  
    - 토핑의 가짓수를 어떻게 갱신?: 딕셔너리에 왼쪽 토핑 가짓수와 오른쪽 토핑 가짓수를 매번 갱신하기 
    - 양쪽 토핑의 가짓수 비교는 어떻게?: 토핑 수가 0이라면 딕셔너리에서 해당 토핑 아예 제거 => 양 딕셔너리의 길이가 토핑 가짓수를 의미하게 됨 
'''
from collections import deque
def solution(topping):
    answer = 0
    
    # 케이크를 이등분한 왼쪽, 오른쪽 
    left_q, right_q = deque(), deque(topping)
    # 왼쪽, 오른쪽의 토핑 수 
    left_dic, right_dic = {}, {}

    # 오른쪽 딕셔너리 초기화 
    for t in topping:
        if t not in right_dic: 
            right_dic[t] = 1
        else:
            right_dic[t] += 1
            
    # 케이크 이등분하기 
    for i in range(len(topping)-1):
        # 오른쪽에서 왼쪽으로 토핑 1개 이동 
        right_t = right_q.popleft()
        left_q.append(right_t)
        
        # 가짓수 갱신 
        # 왼쪽은 토핑 증가, 오른쪽은 토핑 감소 
        if right_t in left_dic:
            left_dic[right_t] += 1
        else:
            left_dic[right_t] = 1
                
        right_dic[right_t] -= 1
        # 해당 토핑이 0개가 된다면 딕셔너리에서 아예 삭제 
        if right_dic[right_t] == 0:
            del right_dic[right_t]
            
        # 양쪽 가짓수 비교: 양쪽 딕셔너리 길이(양쪽 토핑의 가짓수)가 같다면 
        if len(left_dic) == len(right_dic):
            answer += 1
        
    return answer