'''
왼쪽으로 1칸 회전 = 왼쪽으로 1칸씩 밀었다 
'''
from collections import deque
def solution(s):
    answer = 0
    q = deque(s)
    left_b = ['[', '(', '{']
    right_b = {
        ']': 0, 
        ')': 1, 
        '}': 2
    }

    def is_right_bracket(bracket):
        stack = []
        for b in bracket:
            if b in left_b:
                stack.append(b)
            else: # 오른쪽 괄호임 
                if not stack:
                    return False
                p = stack.pop() 
                
                if p not in left_b: # p도 오른쪽 괄호면 실패 
                    return False
                
                idx = right_b[b]
                if left_b.index(p) != idx: # 짝이 안 맞으면 실패 
                    return False
                
        if stack:
            return False
        return True
        
    for i in range(len(s)):
        # 올바른 괄호인지 확인 
        if is_right_bracket(q):
            answer += 1
        
        front = q.popleft()
        q.append(front)

    return answer