def solution(n):
    answer = 0
    
#   반복문 내에서 end 점점 늘려가다가, 타겟에 도달하면 start를 하나 뒤로 이동 
    start = 1
    end = 0
    total = 0
    
#   n(타겟)을 넘어가면 종료 
    while end <= n:
#       total이 타겟보다 크거나 같으면 start 1씩 뒤로 밀기(현재의 start는 total에서 제거) 
        if total >= n:
#           타겟 도달 여부 확인 
            if total == n:
                answer += 1
        
            total -= start
            start += 1

#       total이 타겟보다 작으면 end 1씩 증가 
        elif total < n:
            end += 1
            total += end 
            
    return answer