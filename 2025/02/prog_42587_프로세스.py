'''
*** 숫자가 클수록 우선순위가 높은 것임 
a, b, c, d
2, 1, 3, 2

out: a, False, / b, c, d, a
out: b, False, / c, d, a, b
out: c, True, / d, a, b
out: d, True, / a, b
out: a, True, / b
out: b, True

1. 타겟 프로세스를 True로 표기 
    - [(2, False), (1, False), (3, True), (2, False)]
    
2. 큐에 들어있는 것들과 순위 비교를 어떻게?: 일일히 전체 비교? 안될 것 같음. 
    - 순위 내림차순 정렬해서 큐에 넣기: [3, 2, 2, 1] 
    - top = pri_q.popleft() # 큐에서 pop한 front는 항상 최우선순위임 
    - cur이 top과 일치한다면(cur이 최우선 프로세스라면) 실행, top 갱신
    - cur이 top보다 작다면 무효, cur = wait_q.append() (cur는 다시 대기 큐로)
'''
from collections import deque
def solution(priorities, location):
    answer = 0
    wait_q = deque() # 대기 큐 
    pri_q = deque(sorted(priorities, reverse=True)) # 우선순위 내림차순한 큐 
    top = pri_q.popleft() # 가장 높은 우선순위 
    
    # 대기 큐에 [(우선순위, 타겟여부), ...] 형태로 삽입 
    for i in range(len(priorities)):
        is_target = False
        if i == location:
            is_target = True
        wait_q.append((priorities[i], is_target))
            
    while wait_q:
        cur_pri, cur_is_tar = wait_q.popleft() # 프로세스 우선순위, 프로세스 타겟 여부 
        # 일치, 프로세스 실행 
        if cur_pri == top: 
            answer += 1
            # 프로세스 타겟 여부 확인 
            if cur_is_tar:
                break
            # top 갱신 
            top = pri_q.popleft()
        # 무효, 프로세스 실행하지 않음 
        else:
            # 대기 큐에 재삽입 
            wait_q.append((cur_pri, cur_is_tar))
    
    return answer