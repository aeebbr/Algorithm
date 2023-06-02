# 벽 세 개 세우기: 브루트 포스
# 1) 0으로 된 모든 영역에 벽 세 개씩 세우기
# 2) 세 개 다 세웠다면 바이러스 퍼트리기 

# 바이러스 퍼트리기: bfs 
# 벽 세 개 세워진 배열에 2를 퍼트리기 

# 바이러스 퍼지는 조건
# 0인 곳만
# 탐색 위치가 범위 내여야만

# 안전 영역 크기의 최대값 구하기 
# 배열 다 돌면서 0인 곳 카운트 
# 전역에 있는 최대값보다 크다면 갱신 

# 출력: 안전 최대 크기 출력
# --------------------------------------------------------
import sys
import copy
from collections import deque

input = sys.stdin.readline

# 안전 영역 최대 크기 
max_safe_size = 0

# 사방: 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def print_arr(arr):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print()

def cnt_safe_size(arr):
    safe_size = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                safe_size += 1  

    # 최대 크기 갱신 
    global max_safe_size
    max_safe_size = max(max_safe_size, safe_size)

# 바이러스 퍼트리기: bfs
def spread_virus():
    queue = deque()

    # 큐에 바이러스 전부 넣기
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                queue.append((i, j))


    # 카피 배열에 퍼트리기 
    copy_map = copy.deepcopy(map)

    # 큐에 들어있는 바이러스 전부 탐색
    while queue:
        cr, cc = queue.popleft()
        # 사방 탐색하며 바이러스 위치 찾고, 퍼트리기 
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 조건: 1) 범위 내여야 함, 2) 0이어야 함
            if 0 <= nr < n and 0 <= nc < m and copy_map[nr][nc] == 0:
                # 조건에 맞으면 퍼트리기 
                copy_map[nr][nc] = 2

                # 바이러스 퍼진 곳을 큐에 넣기 
                queue.append((nr, nc))

    # 바이러스 퍼트리기 끝. 안전 영역 세기 
    cnt_safe_size(copy_map)

# 재귀
def build_wall(cnt):
    # 탈출 조건: 벽 개수가 3이라면 바이러스 함수 호출, 종료 
    if(cnt == 3):
        spread_virus()
        return 
    
    # 벽 세우기 
    for cr in range(n):
        for cc in range(m):
            # 조건: 빈 곳(0)인지 
            if map[cr][cc] == 0:
                # 조건에 맞다면 벽 세우기 
                map[cr][cc] = 1
                # 재귀 호출
                build_wall(cnt + 1)
                # 재귀에서 돌아옴(벽이 다 세워진 배열로 안전 크기까지 카운트 끝 -> 다음 벽 조합 만들기) 
                # 벽 없애기(백 트래킹)
                map[cr][cc] = 0

# 입력
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

# 벽 세우기 함수 호출
build_wall(0)

# 결과 출력
print(max_safe_size)

# print_arr(map)

