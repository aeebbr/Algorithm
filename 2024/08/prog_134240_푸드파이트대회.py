'''
좌우 대칭으로 
덱으로 풀이 
'''

from collections import deque
def solution(food):
    q = deque([0])
    
    for i in range(len(food)-1, -1, -1):
        if i == 0:
            break
            
        f = food[i] // 2
        
        if f > 0:
            for j in range(f):
                q.appendleft(i)
                q.append(i)
                
    return "".join(map(str, list(q)))