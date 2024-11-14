def solution(s):
    stack = []
    
    for ss in s:
        if stack:
            p = stack.pop()
            
            if ss != p:
                stack.append(p)
                stack.append(ss)
        else:
            stack.append(ss)

    if stack:
        return 0
    else:
        return 1