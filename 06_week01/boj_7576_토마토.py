import sys 
from collections import deque

input = sys.stdin.readline

# 결과: 날짜 
day = 0

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# def print_arr(arr):
#     for i in range(n):
#         for j in range(m):
#             print(arr[i][j], end=' ')
#         print()

def bfs():
    queue = deque()
    # 익은 토마토를 전부 큐에 넣기 
    for i in range(n):
        for j in range(m):
            if map[i][j] == 1:
                queue.append((i, j))

    # 큐에 있는 토마토 전부 탐색
    # 토마토가 있으면 계속 탐색 
    while queue:
        cr, cc = queue.popleft()

        # 사방 탐색
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < n and 0 <= nc < m and map[nr][nc] == 0:
                queue.append((nr, nc))
                map[nr][nc] = map[cr][cc] + 1

def find_max_day():
    global day
    for i in range(n):
        for j in range(m):
            # 익지 않은 토마토 발견
            if map[i][j] == 0:
                print(-1)
                # 프로그램 종료 
                exit(0)
            else:
                day = max(day, map[i][j])
        
# 입력
m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

bfs()
find_max_day()

# 결과 출력
# 날짜 카운트할 때 첫 날을 2로 시작했으니 1 빼주기 
print(day - 1)