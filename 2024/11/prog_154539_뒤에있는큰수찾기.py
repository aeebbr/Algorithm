def solution(numbers):
    answer = [-1] * len(numbers)
    numbers = numbers[::-1]
    stack = []
    
    for i in range(len(numbers)):
        cur = numbers[i]
        while stack:
            top = stack.pop()
            
            # cur이 top보다 낮다면 top이 cur에 대응
            if cur < top:
                answer[i] = top
                stack.append(top) # top 살아남음 
                break
                
        stack.append(cur)

    return answer[::-1]