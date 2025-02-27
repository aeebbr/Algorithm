'''
1, 2
3, 4(A): 4 -> 2
5, 6
7, 8(B): 7 -> 4

1, 2(A): 2 -> 1
3, 4(B): 4 -> 2

1(A), 2(B): 3라운드에서 만남 

[(1, 1, False), (2, 1, False), (3, 1, False), (4, 1, True), ... ]
'''
from collections import deque
def solution(n,a,b):
    answer = 0

    q = deque() # [(선수번호, 라운드번호, True or False), (...), ... ]
    for nn in range(1, n+1):
        if nn == a or nn == b:
            q.append((nn, 1, True))
        else:
            q.append((nn, 1, False))
            
    while q:        
        i_n, i_r, i_b = q.popleft()
        j_n, j_r, j_b = q.popleft()
        # 이번 라운드의 몇 번째 경기인가? 
        cnt = j_n // 2 
        
        # 둘 다 True라면 
        if i_b and j_b:
            answer = i_r
            break
        # 둘 중 하나만 True라면
        elif i_b or j_b:
            # 다음 라운드에서는 현재의 cnt가 선수의 번호와 동일함
            q.append((cnt, i_r+1, True))
        # 둘 다 False라면 
        else:
            q.append((cnt, i_r+1, False))

    return answer