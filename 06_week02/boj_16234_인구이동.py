import sys
from collections import deque
import math

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

day_cnt = 0

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = " ")
        print()
    print()

def bfs(row, col):
    # 큐 초기화 
    # 사방탐색을 위한 큐
    findQ = deque()
    # 인구이동을 위한 큐
    moveQ = deque() 

    # 출발 지점을 큐에 삽입
    findQ.append((row, col))

    # 방문 처리 
    visited[row][col] = True

    # 연합된 인구 총합
    total_people = map[row][col]
    # 연합된 국가 총합
    total_country = 1

    while findQ:
        # 큐에서 하나 꺼내기 
        cr, cc = findQ.popleft()

        # 사방탐색
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 조건 확인: 1) 배열 범위 내인지, 2) 방문하지 않은 곳인지, 3) 인구 이동 가능 범위 내인지
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if l <= abs(map[cr][cc] - map[nr][nc]) <= r:
                    # 연합되었다면 큐에 삽입
                    findQ.append((nr, nc))
                    moveQ.append((nr, nc))

                    # 방문처리
                    visited[nr][nc] = True

                    # 연합 인구 수에 합
                    total_people += map[nr][nc]
                    # 연합된 국가 수에 합
                    total_country += 1

    # 이동할 인구가 없다면
    if not moveQ:
        return False

    # 인구 이동 가능하다면 출발 지점 삽입
    moveQ.append((row, col))

    # 이동할 인구 계산 
    move_people_cnt = math.trunc(total_people / total_country)

    # 인구 이동 후 True 리턴
    while moveQ:
        mr, mc = moveQ.popleft()

        # 연합된 국가에 인구 이동
        map[mr][mc] = move_people_cnt

    return True

n, l, r = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = []

while True:
    # 방문배열 초기화
    visited = [[False] * n for _ in range(n)]
    # 배열 한 번 탐색(하루)
    isMoved = False

    for i in range(n): 
        for j in range(n): 
            # 방문하지 않은 곳이라면
            if not visited[i][j]:
                if bfs(i, j):
                    isMoved = True
    
    # 하루 끝
    # 인구이동하지 못했다면 반복문 탈출
    if not isMoved:
        break

    day_cnt += 1

print(day_cnt)
