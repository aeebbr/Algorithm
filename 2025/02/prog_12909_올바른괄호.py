def solution(s):
    answer = True

    stack = []
    
    for ss in s:
        if ss == '(':
            stack.append(ss)
        else:
            # stack이 비어있다면 실패 
            if not stack:
                return False
            else:
                stack.pop()
                
    # stack이 차있다면 실패 
    if stack:
        return False
    
    return True