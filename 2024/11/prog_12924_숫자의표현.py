"""  
total이 n이 되면 카운트, end 추가 
total이 n보다 크면 start 제거 
total이 n보다 작으면 end 추가 

기저조건: end가 n보다 커지면 종료 

n이 2라면 
1
1, 2
2
"""
def solution(n):
    answer = 1 # cnt 
    start = 1
    end = 1
    total = start
    
    while end < n:
        if total > n:
            total -= start
            start += 1
        elif total <= n:
            if total == n:
                answer += 1
            end += 1
            total += end
    
    return answer