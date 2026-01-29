# 회전 = 쉬프트 
# 한 바퀴를 회전 

from collections import deque
def solution(s):
    def is_right_bracket(q):
        open_b = ['(', '{', '[']
        close_b = [')', '}', ']']
        stack = []
        
        for b in q:
            if b in open_b:
                stack.append(b)
            else:
                if not stack:
                    return False
                
                idx = open_b.index(stack[-1])
                if b == close_b[idx]:
                    stack.pop()
                else:
                    return False
                
        if stack:
            return False
        return True
    
    answer = 0
    q = deque(list(s))
    
    for _ in range(len(s)):
        if is_right_bracket(q):
            answer += 1
            
        front = q.popleft()
        q.append(front)
    
    return answer