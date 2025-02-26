def solution(n):
    answer = 0
    
    # 연속된 수의 범위: 1 ~ n까지 
    '''
    연속된 수를 누적합 하여 가다가, 
    - 합이 n보다 크다면, 맨 앞의 것을 빼기(범위 줄이기) 
    - 합이 n보다 작다면, 뒤에 숫자를 추가하기(범위 늘이기)
    - 합이 n이라면, answer+= 1 하고 뒤에 숫자 추가(범위 늘이기)
    
    범위는 어떻게 잡나? -> 투 포인터로: left, right
    '''

    left, right = 1, 0
    total = 0 # 누적합 
    # 탈출조건: right가 n보다 클 경우 
    while right <= n:
        if total > n:
            total -= left
            left += 1
        elif total < n:
            right += 1
            total += right
        else:
            answer += 1
            right += 1
            total += right
    
        # print(answer, total, left, right)
    
    return answer