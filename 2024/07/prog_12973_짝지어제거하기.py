'''
스택의 top에 있는 문자가 현재 문자와 같은지 확인
    같다면 그대로 top을 pop
    다르다면 스택에 현재 문자 push 
문자를 모두 탐색했을 때 스택이 비게되면 성공, 아니라면 실패 
'''
def solution(s):
    stack = []

    for cur in s:
        if not stack:
            stack.append(cur)    
            continue
            
        top = stack[-1]

        if top == cur:
            stack.pop()
        else:
            stack.append(cur)    
            
    if stack:
        return 0
    else:
        return 1