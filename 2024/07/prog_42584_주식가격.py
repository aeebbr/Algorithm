# 문제 의도에 맞는 풀이 
# stack
def solution(prices):
    answer = []
    stack = []
    sec = [0] * len(prices)
    
    for i in range(len(prices)):
        cur = prices[i]
        
        # 스택에 있는 것들에 시간 증가시키기 
        for p, idx in stack:
            sec[idx] += 1
            
        # 현재값이 스택에 있는 값보다 작다면 가격 떨어진 것
            # => 스택에 있던 그 값은 더 이상 시간이 증가될 수 없음 => pop 
        while stack and cur < stack[-1][0]:
            stack.pop()

        # 현재의 것을 스택에
        # (값, 인덱스)
        stack.append((cur, i))
    
    return sec

'''
# 이중 for문 
def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        cur = prices[i]
        sec = len(prices) - i - 1
        for j in range(i, len(prices)):
            if cur > prices[j]:
                sec = j - i
                break
        answer.append(sec)
        
    answer.append(0)
    
    return answer
'''