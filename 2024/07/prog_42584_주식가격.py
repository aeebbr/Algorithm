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