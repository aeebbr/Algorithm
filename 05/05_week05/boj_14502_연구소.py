import copy
from collections import deque
import sys 
input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 안전 영역 크기 
max_safe_size = 0

# 벽 세 개
# 0인 모든 위치에 벽 세 개
# 벽 다 놓으면 안전 영역 크기 카운트
# 최대 안전 영역 크기보다 클 때 갱신

def print_map(map):
    for i in range(n):
        for j in range(m):
            print(map[i][j], end=" ")
        print()
    print()

def bfs():
    # 바이러스 퍼트리기 
    # 다 퍼트리면 안전 영역 카운트 
    
    copy_map = copy.deepcopy(map)

    # 큐에 2의 좌표를 모두 삽입
    queue = deque()
    for i in range(n):
        for j in range(m):
            # 바이러스 발견했다면 큐에 삽입
            if copy_map[i][j] == 2:
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()

        # 사방 탐색
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            # 1, 이동한 위치가 범위 내인지 
            # 2, 이동한 위치가 빈 공간(0)인지
            # 두 조건 모두 충족했다면 바이러스 퍼트리기 
            if 0 <= nr < n and 0 <= nc < m and copy_map[nr][nc] == 0:
                copy_map[nr][nc] = 2
                queue.append((nr, nc))

    # 바이러스 퍼트리기 완료 
    # 안전 영역 카운트하기 
    global max_safe_size
    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_map[i][j] == 0:
                safe_cnt += 1

    # 안전 영역 카운트 완료
    # 현재 카운트보다 최소라면 갱신
    max_safe_size = max(max_safe_size, safe_cnt)

# 세운 벽의 개수를 카운트 
def make_wall(cnt):
    # 벽 세 개라면 안전 영역 세기 
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                # 벽 세우기 
                map[i][j] = 1
                make_wall(cnt + 1)
                map[i][j] = 0

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

make_wall(0)

print(max_safe_size)