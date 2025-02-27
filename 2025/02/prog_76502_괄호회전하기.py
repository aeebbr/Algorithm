# 올바른 괄호 문자열이 만들어지는 경우의 수를 출력하기 
from collections import deque
def solution(s):
    answer = 0
    q = deque(list(s))
    
    open_b = ['[', '{', '(']
    close_b  = [']', '}', ')']
    
    def is_perfect_bracket(bracket):
        stack = []
        
        for bb in bracket:
            if bb in open_b:
                stack.append((bb, open_b.index(bb)))
            else:
                if not stack:
                    return False
                top_b, top_n = stack.pop()
                if close_b.index(bb) != top_n:
                    return False
                
        if stack:
            return False
        
        return True
                
    
    for x in range(0, len(s)):
        # 왼쪽으로 1칸 회전 
        front = q.popleft()
        q.append(front)
        
        # 회전한 결과 올바른 괄호인가? 
        if is_perfect_bracket(q):
            answer += 1
    
    return answer