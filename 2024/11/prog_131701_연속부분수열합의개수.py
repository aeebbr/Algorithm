from collections import deque
def solution(elements):
    answer = []
    
    for i in range(1,len(elements)+1):
        deq = deque(maxlen=i) # 최대 i개만큼만 요소를 추가할 수 있음 
        for j in elements * 2: # 리스트 두 번 반복 
            deq.append(j)
            answer.append(sum(deq))

    return(len(set(answer)))