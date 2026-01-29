# 괄호 문제와 유사. 스택으로 풀이 
# 현재 문자가 스택의 top과 동일하다면 pop, 
#   동일하지 않다면 현재 문자 push 
# 마지막에 스택이 비었다면 1, 아니라면 0 return 
def solution(s):
    stack = []
    
    for cur in s:
        if len(stack) == 0:
            stack.append(cur)
        else:
            top = stack[-1]
            if top == cur:
                stack.pop()
            else:
                stack.append(cur)
                
    if len(stack) == 0:
        return 1
    else:
        return 0