def solution(n):
    ans = 0 # 사용량 
    
    # n에서부터 역으로 탐색 
    while n > 0:
        if n % 2 == 0: # 순간이동의 역이동
            n //= 2
        else: # 한 칸 이동의 역이동 
            n -= 1
            ans += 1
            
    return ans