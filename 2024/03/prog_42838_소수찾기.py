total = []

def perm(idx, cur, visited, numbers):
    global total 
        
    if cur != '':
        total.append(int(cur))
    for i in range(len(numbers)):
        if visited[i]:
            continue
        tmp = cur + numbers[i]
        visited[i] = True
        perm(i+1, tmp, visited, numbers)
        visited[i] = False
            
def prime(cur):    
    '''
    8이라면, 
    1부터 8까지 나눴을 때, 나누어 떨어지는 것 찾기 
    => 1, 2, 4, 8
    => 2개가 아니라면 소수가 아님 
    
    7이라면, 
    => 1, 7
    => 2개니까 소수임 
    
    1부터 N까지 나눌 필요 없이, (N/2 + 1)까지 나누고,
    이 때의 개수가 1개라면 소수임 
    '''
    
    cnt = 0
    for i in range(1, cur//2+1):
        if cur % i == 0:
            cnt += 1
            
    if cnt == 1:
        return True
    else:
        return False
        
def solution(numbers):
    global total 
    
    answer = 0
    numbers = list(numbers)
    visited = [False] * len(numbers)
    # 순열
    perm(0, '', visited, numbers)
    total = list(set(total))
    
    # 소수 판별
    for n in total:
        if n == 0:
            continue
        if prime(n):
            answer += 1       
    
    return answer