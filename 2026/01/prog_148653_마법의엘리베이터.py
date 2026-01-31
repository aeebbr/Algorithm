'''
덧셈이나 뺄셈 연산으로 각 자리수 0 만들기
    이 때, 1의 자리수부터 위로 올라가야 함 

16을 20으로 만들거나, 10으로 만들기 
    이 때, 20으로 만드는 게 더 적게 이동함 
    
2554의 경우,
    2554를 3000으로 만들기 
    -4 -> 2550
    +50 -> 2600
    +400 -> 3000
    -3000 -> 0
    
    혹은 
    -4 -> 2550
    -50 -> 2500
    -500 -> 2000
    -2000 -> 0
'''
def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))
    
    for i in range(len(storey)-1, -1, -1):
        num = storey[i]
            
        if num < 5:
            # num 빼기가 유리(ex. num=2) 
            answer += num
        elif num > 5:
            # 10-num 더하기가 유리(ex. num=8)
            answer += (10-num)
            
            # 제일 높은 자리의 올림이라면, 자리수 하나 더 증가
            # => 증가되는 다음 자릿수인 1을 버리는 경우의 수를 하나 증가
            if i == 0:
                answer += 1
            else:                
                storey[i-1] += 1
        else:
            # 15 -> 20 
            # 15 -> 10 이게 유리 
            
            # 65 -> 70 이게 유리 
            # 65 -> 60 
            
            # 55 -> 60 이게 유리 
            # 55 -> 50
            if storey[i-1] < 5:
                # 빼기가 유리 
                answer += num
            else:
                # 더하기가 유리 
                answer += num
                storey[i-1] += 1
            
        storey[i] = 0
            
    return answer