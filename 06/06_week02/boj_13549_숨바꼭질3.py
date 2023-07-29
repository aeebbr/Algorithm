import sys 
from collections import deque

input = sys.stdin.readline

# 수빈이가 이동할 수 있는 모든 범위를 방문 배열로 
# -1은 미방문, 0부터는 각 노드까지 걸린 시간
visited = [-1 for _ in range(100001)]
q = deque()

# bfs
# 앞으로 걷기, 뒤로 걷기, 순간이동
# 세 가지 경우를 모두 행하기 
# ex) 5 -> 17
# 앞으로: 6, 뒤로: 4, 순간이동: 10

# 이 때, 최단 시간을 구하는 것이니 0초가 걸리는 순간이동을 가장 우선시해야 함
# -> 순간이동은 큐의 맨 앞에, 나머지는 큐에 뒤에서 삽입
def bfs():
    while q:
        # 현재 위치 
        cur = q.popleft()
        
        # 동생에게 도달했다면 성공
        if cur == k:
            print(visited[cur])
            return 

        # 뒤로 1칸 걷기
        # 이동한 지점이 1) 범위 내인지, 2) 방문하지 않은 곳인지  
        if 0 <= cur-1 < 100001 and visited[cur-1] == -1:
            # 방문 처리 
            # 소요된 시간 추가
            visited[cur - 1] = visited[cur] + 1
            # 큐에 이동 지점 삽입
            q.append(cur - 1)

        # 순간이동이 앞으로 1칸보다 먼저 실행되어야 한다 
        # cur = 2일 때, 순간이동과 앞으로 1칸 모두 2로 이동하기 때문에, 먼저 실행되는 조건문에서 방문 처리를 선수치므로
        # 뒤에 오는 조건문은 실행되지 않는다 
        
        # 순간 이동
        # 0에서는 순간 이동을 할 수 없기 때문에(0 * 2 = 0) 범위를 1부터
        if 0 < cur * 2 < 100001 and visited[cur * 2] == -1:
            # 순간 이동은 시간이 걸리지 않음
            visited[cur * 2] = visited[cur]
            q.appendleft(cur * 2)
        # 앞으로 1칸 걷기 
        if 0 <= cur + 1 < 100001 and visited[cur + 1] == -1:
            visited[cur + 1] = visited[cur] + 1
            q.append(cur + 1)
            
n, k = map(int, input().split())

# 수빈이의 시작 지점을 방문 처리하면서 0초로 초기화
visited[n] = 0
# 큐에 시작 지점 삽입
q.append(n)

bfs()
