from collections import deque
def solution(x, y, n):
    q = deque([(x, 0)]) # (num, cnt)
    # 방문배열 범위: 1에서부터 y까지 
    visited = [False for _ in range(y+1)]
    visited[x] = True
    
    while q:
        num, cnt = q.popleft()

        if num == y:
            return cnt

        for i in range(3):
            if i == 0:
                tmp = num + n
            elif i == 1:
                tmp = num * 2
            else:
                tmp = num * 3
                
            if tmp > y or visited[tmp]:
                continue 
                
            q.append((tmp, cnt+1))
            visited[tmp] = True

    return -1 