# 백준 레이저 탑같은 문제...? -> 스택? 

# 스택: 가능성 있는 것만 담기 
# 역방향에서부터 순회
    # 현재 수보다 큰 수만 스택에 담기 
    
    # 스택에서 pop, 현재보다 크면 result에 저장하고 다시 push 
    # 현재 수도 push 
def solution(numbers):
    answer = []

    numbers = numbers[::-1]
    stack = []
    
    for cur in numbers:
        isFind = False
        while stack:
            top = stack.pop()

            if cur < top:
                answer.append(top)
                isFind = True
                stack.append(top)
                break
        
        if not isFind:
            answer.append(-1)
        
        stack.append(cur)
    
    answer = answer[::-1]
    return answer