# dfs로 풀이 

# 1번 컴퓨터에서 시작 
# 양방향 연결 리스트

import sys 
input = sys.stdin.readline

# 바이러스 걸리는 수 
cnt = 0

# cur: 현재 컴퓨터 
def dfs(cur):
    global cnt
    visited[cur] = True

    # 현재 컴퓨터에 연결되어 있는 컴퓨터 탐색
    for link in computer[cur]:
        # 컴퓨터의 방문 여부 확인
        if visited[link]:
            continue

        cnt += 1
        dfs(link)

# 입력
C = int((input()))
PAIR = int((input()))

computer = [[] for _ in range(C + 1)]
visited = [False] * (C + 1)

for _ in range(PAIR):
    a, b = map(int, input().split())
    # 각 컴퓨터에 연결된 컴퓨터 표시 
    computer[a].append(b)
    computer[b].append(a)

# 1번 컴퓨터에서 시작 
dfs(1)
print(cnt)