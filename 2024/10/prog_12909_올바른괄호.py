from collections import deque

def solution(s):
    q = deque()
    
    for b in s:
        if b == "(":
            q.append(b)
        else:
            if not q:
                return False
            
            q.popleft()

    if q:
        return False
    
    return True