from collections import deque

def bfs(start, computers, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        cur = q.popleft()
        
        for next in range(len(computers[cur])):
            if not visited[next] and computers[cur][next] == 1:
                q.append(next)
                visited[next] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(len(computers)):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
    
    return answer