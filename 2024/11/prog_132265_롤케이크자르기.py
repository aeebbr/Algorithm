# 토핑 개수가 아니고 종류 수 따지기 
from collections import deque
def solution(topping):
    answer = 0
    slice_1 = deque()
    slice_2 = deque(topping)
    dic_1 = {}
    dic_2 = {}
    
    for e in slice_2:
        if e in dic_2:
            dic_2[e] +=1
        else:
            dic_2[e] =1
    
    for i in range(len(topping)-1):    
        front = slice_2.popleft()
        slice_1.append(front)
        
        # slice_1 삽입
        if front not in dic_1:
            dic_1[front] = 1
        else:
            dic_1[front] += 1
            
        # slice_2 제거  
        dic_2[front] -= 1
        if dic_2[front] == 0:
            del dic_2[front]
    
        if len(dic_1) == len(dic_2):
            answer += 1

    return answer