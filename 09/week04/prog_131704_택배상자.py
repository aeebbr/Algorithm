# 4, 3, 1, 2, 5 에서 cur에 현재 인덱스 저장  
# 1, 2, 3, 4, 5 순회하면서 
    # cur이 아니라면 보조 큐에 저장 
    # cur이라면 저장 없음, answer 1 증가, 현재 인덱스 갱신 
# 순회 다 했다면 보조 큐 순회 
    # 보조 큐 pop 했을 때 cur이 아니라면 프로그램 종료 
from collections import deque
    
def solution(order):
    answer = 0
    spare_q = deque()
    cur_idx = 0
    
    for n in range(1, len(order)+1):
        # 보조 큐 확인 
        if spare_q:
            pop = spare_q.pop()
            # 보조 큐에서 뺄 수 있다면 빼기 
            if pop == order[cur_idx]:
                answer += 1
                cur_idx += 1
            # 뺄 수 없다면 pop 다시 넣고, 보조 큐에 상자 넣기 
            else:
                spare_q.append(pop)
                
        if n == order[cur_idx]:
            answer += 1
            cur_idx += 1
        elif n != order[cur_idx]:
            spare_q.append(n)
        
    while spare_q:
        pop = spare_q.pop()
        
        if pop != order[cur_idx]:
            break
        else:
            answer += 1
            cur_idx += 1
    
    return answer