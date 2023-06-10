# 검을 구하는 경우, 구하지 못하는 경우로 나누고, 둘 중 최단 거리를 고르기 

# 출발 지점에서부터 최단거리로 가기 
# 가다가 검을 구하면 => (출발에서 검까지의 거리) + (검에서 도착까지의 최소거리)
# 그리고는 검을 구하지 못한 경우를 가정하고 도착까지 가기 

import sys 
from collections import deque

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def print_arr(arr):
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end = " ")
        print()
    print()

def bfs():
    # 시간
    # 검 없이 가는 시간
    time_without_gram = 0
    # 검이랑 가는 시간
    # 최소값을 구해야 하니 양의 최대값으로 초기화
    time_with_gram = float('inf')

    # 큐 초기화 
    q = deque()

    # 큐에 시작 지점 삽입
    q.append((0, 0))
    # 시작 지점 방문 처리 
    visited[0][0] = True

    # 반복 조건
    # 1) 이동할 지점이 남아있을 것
    # 2) 검 없이 걸리는 시간이 T보다 적을 것
    while q and time_without_gram <= T:
        # 한 사이클: 한 시간 
        for _ in range(len(q)):
            # 큐에서 하나 빼기 
            cr, cc = q.popleft()

            # 현재 지점이 도착 지점이라면 종료
            if cr + 1 == N and cc + 1 == M:
                # 검 있는 경우와 없는 경우 중 최단 시간을 리턴
                return min(time_with_gram, time_without_gram)

            # 사방 탐색
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]

                # 이동 조건: 1) 범위 내일 것, 2) 방문하지 않았을 것
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    # 3) 검일 것 
                    if map[nr][nc] == 2:
                        # 검을 발견하면 (시작 ~ 검까지의 시간) + (검 ~ 도착까지의 최단 시간)
                        gram_to_goal = abs(N - 1 - nr) + abs(M - 1 - nc) + 1
                        time_with_gram = time_without_gram + gram_to_goal

                        # 검의 위치를 0으로 바꿔야 검 없이 가는 경우로 이어짐
                        map[nr][nc] = 0

                    # 3) 빈 공간일 것
                    if map[nr][nc] == 0:
                        # 이동 지점 큐에 삽입 
                        q.append((nr, nc))
                        visited[nr][nc] = True

        # 한 시간 끝, 시간 증가 
        time_without_gram += 1

    # 여기 까지 왔다는 것은 
    # 1) 검 없이 가는 경우가 시간 내든 아니든 도착 지점까지 가지 못한 경우

    # 따라서, 검으로 도착까지 간 경우를 따져야 함
    # 검으로도 시간을 초과한 경우
    if time_with_gram > T:
        return 'Fail'
    # 검으로 시간 내에 도착한 경우
    else:
        return time_with_gram

# 입력
N, M, T = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

print(bfs())

