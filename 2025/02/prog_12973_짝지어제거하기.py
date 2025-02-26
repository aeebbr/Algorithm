def solution(s):
    stack = []
    
    for cur in s:
        # 스택에 있는 마지막 문자가 현재와 같은지 확인 
        if stack:
            top = stack[-1]
            if top == cur:
                stack.pop()
            else:
                stack.append(cur)
        else:
            stack.append(cur)
                
    if stack:
        return 0
    else:
        return 1