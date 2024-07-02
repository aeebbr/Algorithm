def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        # stack = [... 1, 2, 3], i = 1이라면 
        if i == 1 and len(stack) >= 3 and stack[-1] == 3 and stack[-2] == 2 and stack[-3] == 1:
            answer += 1
            # stack에서 햄버거 제거 
            for _ in range(3):
                stack.pop()
        else:
            stack.append(i)    
            
    return answer