from collections import deque

def solution(n):
    answer = 1
    
    q = deque()
    total = 0 # q의 총합 
    num = 1 # 더하는 자연수 
    
    while True:
        if total == n:
            answer += 1
            
        # 만약 n보다 크다면 q에서 수를 뻬야 함
        elif total > n:
            pl = q.popleft()
            total -= pl
            continue 
            
        '''
        이 탈출문을 while 시작부에 적으면 안됨 
        <반례>
        n = 3의 경우,
        result = 2 (1+2=3, 3=3)
        이어야 하지만 
        result = 1 (3=3) 만 나옴 
        '''
        if num == n:
            break

        # 큐에 num을 계속 더하기 
        q.append(num)
        total += num
        num += 1 
    
    return answer