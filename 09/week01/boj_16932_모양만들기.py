import sys 
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc):
    global visited
    
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = group_num

    cnt = 1

    while q:
        cr, cc = q.popleft()
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = group_num
                    cnt += 1

    return cnt 

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dic = {}

group_num = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            dic[group_num] = bfs(i, j)
            group_num += 1

max_size = 0

# board 순회하며 0 찾고, 0의 사방탐색해서 인접한 1 찾기 
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            group_set = set()
            # 사방탐색
            for dir in range(4):
                nr = i + dr[dir]
                nc = j + dc[dir]

                # 범위 내, 방문했을 것 = 1일 것 
                # 현재 지점과 이어져있는 덩어리라면 그룹넘버 저장 
                # if 0 <= nr < N and 0 <= nc < M:
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]:
                    num = visited[nr][nc]
                    group_set.add(num)

            # 사방탐색 끝 
            # 인접해있는 그룹의 크기 계산하기 
            size = 1
            for group in group_set:
                size += dic[group]

            # 최대값 갱신 
            max_size = max(max_size, size)

print(max_size)

########################################################################

# import sys 
# input = sys.stdin.readline
# from collections import deque

# # 우 하 좌 상
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# def bfs(sr, sc):
#     global visited, dic, group_size
#     q = deque()
#     q.append((sr, sc))
#     visited[sr][sc] = True
#     cnt = 1
#     group_num = len(group_size)

#     while q:
#         cr, cc = q.popleft()
#         for dir in range(4):
#             nr = cr + dr[dir]
#             nc = cc + dc[dir]

#             if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
#                 if board[nr][nc] == 1:
#                     q.append((nr, nc))
#                     visited[nr][nc] = True
#                     cnt += 1
#                 else:
#                     if (nr, nc) not in dic:
#                         dic[(nr, nc)] = [group_num]
#                     elif (nr, nc) in dic and not group_num in dic[(nr, nc)]:
#                         dic[(nr, nc)].append(group_num)

#     group_size.append(cnt)
    
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
# dic = {}
# group_size = []

# # 모든 지점 순회하며 1 덩어리 찾기 
# for i in range(N):
#     for j in range(M):
#         if board[i][j] == 1 and not visited[i][j]:
#             bfs(i, j)

# # 0이 하나도 없었다면 
# if len(dic) == 0:
#     # 1 덩어리가 하나라는 것 
#     print(group_size[0])
#     exit()

# max_value = []
# # dic에서 크기가 가장 큰 값을 가진 키의 값들 찾기 
# # 그 값들의 group_size 더하기 
# for value in dic.values():
#     if len(max_value) < len(value):
#         max_value = value
#     # 같을 경우에는? 
#     # 속한 그룹 크기가 큰 것들을 채택 
#     elif len(max_value) == len(value):
#         # 기존 최대 그룹 크기 
#         cur_max_size = 0
#         for i in max_value:
#             cur_max_size += group_size[i]
#         # 새로운 그룹 크기 
#         new_size = 0
#         for i in value:
#             new_size += group_size[i]

#         if new_size > cur_max_size:
#             max_value = value

# # max_value들의 그룹 길이 합 + 1이 답임
# answer = 0
# for group in max_value:
#     answer += group_size[group]

# # 덩어리가 하나가 아니라면 = 연결할 덩어리들이 있다면, 연결지점까지 포함해야 하니 +1함 
# if len(max_value) == 1:
#     print(answer)
# else:
#     print(answer + 1)

################################################################

# # 한 번만 1로 바꿀 수 있음 
# # 우하좌상이 1로 연결되어 있는 덩어리의 최대 길이 
# # bfs, 3차원 방문 배열로 1) 1로 바꾸지 않은 경로, 2) 1로 바꾼 경로 나누기 

# import sys 
# input = sys.stdin.readline
# from collections import deque

# # 우 하 좌 상
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# def bfs(sr, sc):
#     q = deque()
#     # 3차원 방문 배열에 카운트 저장 
#     # [r][c][0]: 1로 바꾸지 않은 경로의 카운트, [r][c][1]: 1로 바꾼 경로의 카운트  
#     visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

#     q.append((sr, sc, 0))
#     visited[sr][sc][0] = 1
#     cnt = 0

#     while q:
#         # route: 경로 종류
#         cr, cc, route = q.popleft()
        
#         for dir in range(4):
#             nr = cr + dr[dir]
#             nc = cc + dc[dir]

#             # 조건
#             # 범위 내, 미방문
#             if 0 <= nr < N and 0 <= nc < M :
#             # if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc][route]:
#                 # 0일 경우: 경로 0이라면 경로 1로 전환
#                 if board[nr][nc] == 0 and route == 0 and not visited[nr][nc][route]:
#                     q.append((nr, nc, 1))
#                     # 지금까지의 카운트는 현재 지점 경로 0의 방문 배열에 저장되어 있음 
#                     visited[nr][nc][1] = visited[cr][cc][0] + 1
#                     cnt += 1
#                 # 1일 경우: 경로 상관 없이 미방문했다면 현재 경로로 이동 
#                 elif board[nr][nc] == 1 :
#                 # elif board[nr][nc] == 1 and not visited[nr][nc][route]:
#                     q.append((nr, nc, route))
#                     # 경로 전환 없기 때문에 현재 지점의 현재 경로에 저장된 카운트에서 1증가  
#                     visited[nr][nc][route] = visited[cr][cc][route] + 1
#                     cnt += 1

#         # 큐 비었다면 종료, 카운트 리턴 
#         if not q:
#             # 마지막 지점의 경로에 저장되어 있는 카운트를 출력 
#             # 0의 총 카운트, 
#             # 1의 총 카운트 
#             return cnt 

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]

# print(bfs(0, 0))