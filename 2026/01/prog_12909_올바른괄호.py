# 스택으로 해결
    # 닫는 괄호 -> 스택 push
    # 여는 괄호 -> 스택 pop
    # 마지막에 스택에 남아있으면 -> F

def solution(s):
    stack = []
    
    for i in range(len(s)):
        b = s[i]
        
        if b == '(':
            stack.append(b)
        else:
            if len(stack):
                stack.pop()
            else:
                return False
        
    if len(stack):
        return False
    
    return True