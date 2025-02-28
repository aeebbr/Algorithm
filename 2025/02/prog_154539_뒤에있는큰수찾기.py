'''
백준의 '레이저 탑'과 유사한 문제 
스택 
뒤에서부터 탐색 
'''
from collections import deque
def solution(numbers):
    q = deque()
    stack = []
    
    for i in range(len(numbers)-1, -1, -1):
        n = numbers[i]        
        
        if not stack:
            q.appendleft(-1)
            stack.append(n)
            continue
            
        while True:
            if not stack: 
                stack.append(n)
                q.appendleft(-1)
                break
            
            # top = stack[-1]
            top = stack.pop()
            
            # top이 답임
            if n < top:
                q.appendleft(top)
                # 스택에 현재 것을 넣기 
                stack.append(top)
                stack.append(n)
                break
                
            # 다음으로 이동 
            
        # 스택에 있는 것을 모두 비교했는데도 못 찾았다 = 뒷큰수가 없다 
        else:
            q.appendleft(-1)
            
    return list(q)