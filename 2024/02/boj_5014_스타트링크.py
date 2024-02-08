from collections import deque

# bfs로 풀이 
    # 단거리(최솟값) 도달은 bfs로!!! 
def bfs():
    q = deque()
    q.append((S, 0))
    # 건물 전층에 대한 방문 배열, 1 ~ F층
    visited = [0] * (F + 1)
    visited[S] = True
    cnt = 0

    while q:
        cur, cnt = q.popleft()

        if cur == G:
            return str(cnt)

        for dir in range(2):
            next = cur + button[dir]
            if 0 < next <= F and not visited[next]:
                q.append((next, cnt + 1))
                visited[next] = True

    return "use the stairs" 

F, S, G, U, D = map(int, input().split())
button = [U, -D]
answer = float("inf")

if G != S:
    print(bfs())
else:
    print(0)
    
'''
# DFS로 풀이: 기저 조건을 잡을 수 없어서 재귀 탈출 안됨 
F, S, G, U, D = map(int, input().split())
button = [U, -D]
answer = float("inf")

def dfs(cur, cnt, tmp):
    global answer
    # 성공
    if cur == G:
        print(cnt, tmp, sum(tmp))
        answer = min(answer, cnt)
        return 
    # 실패 
    if cur < 1 or cur >= F or cnt >= answer or cnt > 10:
        return 
    
    for i in range(2):
        tmp.append(button[i])
        dfs(cur + button[i], cnt + 1, tmp)
        tmp.pop()

dfs(S, 0, [S])
if answer == float("inf"):
    print("use the stairs")
else:
    print(answer)'''