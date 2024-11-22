'''
stack = [], cur = 3 // => // stack = [3]
stack = [3], cur = 2, top = 3 // => // stack = [2]
stack = [2], cur = 3, top = 2 // => // stack = [2] *** 
stack = [2], cur = 2, top = 2 // => // stack = [2]
stack = [2], cur = 1, top = 2 // => // stack = [1] *** 
'''

def solution(prices):
    answer = []
    stack = []
    prices = prices[::-1]
    
    for i in range(len(prices)):
        cur = prices[i]
        is_find = False
        
        while stack:
            top, idx = stack.pop()

            if cur > top:
                answer.append(i - idx)
                stack.append((top, idx))
                is_find = True
                break
                
        stack.append((cur, i))
                
        if not is_find: # 끝까지 가격 안 떨어짐 
            answer.append(i)

    return answer[::-1]