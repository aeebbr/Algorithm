from collections import deque

def solution(s):
    answer = True

    q = deque()
    
    for b in s:
        if b == '(':
            q.append('(')
        else:
            if not q:
                return False
            if q.pop() != '(':
                return False
            
    if q:
        return False
    
    return True