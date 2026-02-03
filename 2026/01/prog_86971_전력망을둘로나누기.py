'''
1: 3
2: 3
3: 1, 2, 4
4: 3, 5, 6, 7
5: 4
6: 4
7: 4, 8, 9
8: 7
9: 7
'''
from collections import deque
def solution(n, wires):
    answer = 101
    
    linked = [[] for _ in range(n+2)]
    
    for a, b in wires:
        linked[a].append(b)
        linked[b].append(a)
    
    def bfs(a, b):
        q = deque()
        q.append(1)
        visited = [False for _ in range(n+2)]
        visited[1] = True
        cnt = 1
        
        while q:
            cur = q.popleft()
            
            for node in linked[cur]:
                if not visited[node]:
                    if (cur, node) != (a, b) and (node, cur) != (a, b):
                        q.append(node)
                        visited[node] = True
                        cnt += 1
        return cnt
        
    for a, b in wires:
        cnt = bfs(a, b)
        tmp = max(cnt, n-cnt) - min(cnt, n-cnt)
        answer = min(answer, tmp)
    
    return answer