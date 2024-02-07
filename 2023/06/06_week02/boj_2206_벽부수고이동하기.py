# 시작에서 도착까지 최단 거리를 구하는 대신, 벽을 한 번 부수고 갈 수 있음

# 경로는 두 가지
    # 1) 벽을 부순 경로, 2) 벽을 부수지 않은 경로 

# 각 경로마다 이동 거리를 저장 
# 각 경로로 이동하다가 벽을 만났을 때,
    # 1) 벽을 부수지 않은 경로라면(기회가 남아있다면) => 부수기
    # 2) 벽을 부순 경로라면(기회가 남아있지 않다면) => 멈춤

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    # 큐 초기화 
    q = deque()

    # 큐에 시작 위치, 벽 부술 기회 삽입
        # 벽을 부수지 않았다면 0, 부쉈다면 1
    q.append((0, 0, 0))
    # 시작 지점 방문 처리
    # 벽 부수지 않은 경로에 방문
    visited[0][0][0] = 1
    
    while q:
        # 큐에서 하나 꺼내기
        # 현재 위치, 경로 종류 
        cr, cc, route = q.popleft()

        # 도착했다면 현재 경로에 저장된 거리를 리턴
        if cr == N - 1 and cc == M - 1:
            return visited[cr][cc][route]
        
        # 사방 탐색
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 이동 조건
            # 1) 범위 내일 것, 2) 방문하지 않았을 것
            if 0 <= nr < N and 0 <= nc < M:
                # 벽이고 벽을 부수지 않은 경로라면(벽 부술 기회가 있다면) 부수기
                if map[nr][nc] == 1 and route == 0:
                    # 벽 부쉈다는 것 체크하여 큐에 삽입
                    q.append((nr, nc, 1))

                    # 방문 처리: 이동 거리 갱신
                    # 벽을 부순 경로에, 여태껏 부수지 않았던 경로의 거리 + 1
                    visited[nr][nc][1] = visited[cr][cc][0] + 1

                # 빈 곳이고, 벽을 부쉈든 아니든 방문하지 않았다면 
                # 한 번이라도 방문했다면 현재 경로(route)의 거리 값은 1 이상임
                elif map[nr][nc] == 0 and visited[nr][nc][route] == 0:
                    q.append((nr, nc, route))

                    # 방문 처리 
                    # 탐색 지점에 현재 경로의 거리 + 1
                    visited[nr][nc][route] = visited[cr][cc][route] + 1

    # 도착하지 못했다면 
    return -1

# 입력
N, M = map(int, input().split())
# 한 행 입력 간의 띄어쓰기가 없음
map = [list(map(int, input())) for _ in range(N)]
# 방문 배열: 3차원, [[[방문 여부, 벽 부술 기회 여부], [...]], ...]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

print(bfs())