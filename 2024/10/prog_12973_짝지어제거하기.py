# 스택 
def solution(s):
    answer = -1
    stack = []
    
    for ss in s:
        if stack:
            top = stack[-1]
            if top == ss:
                stack.pop()
                continue
        
        stack.append(ss)

    if stack:
        return 0
    else:
        return 1