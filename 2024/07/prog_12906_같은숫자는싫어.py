def solution(arr):
    stack = []
    
    for a in arr:
        if stack:
            top = stack[-1]
            if top == a:
                continue
        stack.append(a)
    
    return stack