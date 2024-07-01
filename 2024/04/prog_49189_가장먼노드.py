from collections import deque

def bfs(n, edge, linked_list):
    q = deque()
    q.append((1, 0))
    visited = [False] * (n+1)
    visited[1] = True
    answer = [0] * (n+1)
    
    while q:
        cur, cnt = q.popleft()
        
        if answer[cur] == 0:
            answer[cur] = cnt
        
        for i in range(1, len(linked_list[cur])):
            next = linked_list[cur][i]
            
            if not visited[next]:
                q.append((next, cnt + 1))
                visited[next] = True
                
    return answer.count(max(answer))
        
def solution(n, edge):
    linked_list = [[0] for _ in range(n+1)]
    
    for a, b in edge:
        linked_list[a].append(b)
        linked_list[b].append(a)
    
    return bfs(n, edge, linked_list) 
    