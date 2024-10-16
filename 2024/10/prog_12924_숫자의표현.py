def solution(n):
    answer = 0
    
    '''
    1부터 n까지 더하기 
    투포인터 이용 
    '''
    
    if n == 1:
        return 1
    
    arr = list(range(1, n+1))
    left = 0
    right = 1
    
    while right != n:
        if arr[right] == n:
            answer += 1
            break
            
        total = sum(arr[left:right+1])
        
        if total <= n:
            right += 1
            
            if total == n:
                answer += 1
        elif total > n:
            left += 1
            
    return answer