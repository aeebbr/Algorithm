# 완탐 
# 두 그룹의 노드 개수의 차이의 최소값을 갱신
# wires에서 연결된 배열을 하나씩 없애면서 탐색 
# 탐색은 bfs로 

from collections import deque

def bfs(link_node, linked_list, n):
    q = deque()
    # 시작은 무조건 1부터 
    q.append(1)
    visited = [False] * (n+1)
    visited[1] = True
    a, b = link_node
    
    while q:
        cur = q.popleft()
        
        for i in range(1, len(linked_list[cur])):
            next = linked_list[cur][i]
            if not visited[next] and not ((cur, next) == (a, b) or (cur, next) == (b, a)):
                q.append(next)
                visited[next] = True
    
    return visited.count(True)
    
    
def solution(n, wires):
    answer = float("inf")
    
    linked_list = [[0] for _ in range(n+1)]
    
    for a, b in wires:
        linked_list[a].append(b)
        linked_list[b].append(a)
        
    for link_node in wires:
        # 현재의 연결을 빼고 bfs 탐색 
        link_cnt = bfs(link_node, linked_list, n)
        other_cnt = n - link_cnt
        
        answer = min(answer, (max(link_cnt, other_cnt) - min(link_cnt, other_cnt)))
                   
    
    return answer