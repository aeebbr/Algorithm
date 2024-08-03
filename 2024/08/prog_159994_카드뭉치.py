from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for g in goal:
        if q1:
            c1 = q1.popleft()
            if c1 == g:
                continue
            else:
                q1.appendleft(c1)
        if q2:
            c2 = q2.popleft()
            if c2 != g:
                return "No"
            else:
                continue
        return "No"
    
    return "Yes"