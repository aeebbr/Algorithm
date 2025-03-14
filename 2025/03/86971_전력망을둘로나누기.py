from collections import deque
def solution(n, wires):
    def bfs(start, seperate): 
        q = deque()
        q.append((start))
        visited = [[] for _ in range(n+1)] # 방문 배열 
        visited[start] = True
        a, b = seperate
        cnt = 1
        
        while q: 
            cur = q.popleft()
            
            # 현재 원소와 연결된 원소 모두 탐색 
            for link in graph[cur]:
                if not visited[link]:
                    # 끊을 지점은 연결되지 않은 것과 같은 취급  
                    if ((cur, link) == (a, b)) or ((cur, link) == (b, a)):
                        continue
                    q.append((link))
                    visited[link] = True
                    cnt += 1
                    
        return cnt
        
    answer = 101 # n이 최대 100이기 때문 
    graph = [[] for _ in range(n+1)] # 인접 리스트 
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for w in wires:
        a = bfs(1, w)
        b = n-a
        answer = min(answer, (max(a, b) - min(a, b)))
    
    return answer