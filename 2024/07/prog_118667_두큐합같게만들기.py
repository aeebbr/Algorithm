from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    '''
    실패한 경우: 특정 횟수 이상 작업했는데도 성공하지 못한 경우 

    (최초, 0회)
    1, 1 => 2
    1, 5 => 6

    1, 1, 1 => 3
    5 => 5

    1, 1, 1, 5 => 8
    => 0

    1, 1, 5 => 7
    1 => 1

    1, 5 => 6
    1, 1 => 2

    5 => 5
    1, 1, 1 => 3

    => 0
    1, 1, 1, 5 => 8

    1 => 1
    1, 1, 5 => 7

    1, 1 => 2
    1, 5 => 6
    ---------------
    8회차에 원점으로 돌아옴

    최악의 경우를 실패 기준으로 정해야 함 
    최악의 경우: 원점으로 돌아오는 경우
    하나의 큐의 요소가 다른 큐에 전체 이동 -> 다시 원상태로 돌아오는 경우
    이 때의 횟수: 큐 길이 * 4  
    '''
    limit = len(queue1) * 4
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 매번 큐에 sum()을 쓰지 않기 위함 
    sum1 = sum(q1)
    sum2 = sum(q2)

    # 무조건 실패하는 경우: 두 큐의 합이 홀수인 경우 
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    while True:
        if answer == limit:
            return -1
            
        # 1의 합이 크면 2로 원소 이동, 
        # 2의 합이 크면 1로 원소 이동 
        if sum1 > sum2:
            p = q1.popleft()
            q2.append(p)
            sum1 -= p
            sum2 += p
        elif sum1 < sum2:
            p = q2.popleft()
            q1.append(p)
            sum1 += p
            sum2 -= p
        else: # 성공
            break 
            
        answer += 1
        
    return answer