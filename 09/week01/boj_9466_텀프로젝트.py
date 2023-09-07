# 사이클이 완성되어야만 팀 성사 
# 내가 나를 선택하는 것도 사이클 

# 사이클 체크하고, 전체에서 사이클 인원 뺀 나머지 출력 
# bfs
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global visited

    q = deque()
    q.append(start)
    # {학생: 인덱스넘버}
    # 학생의 인덱스 넘버를 찾는 탐색 속도를 위해 딕셔너리로 
    route = {start: 0}

    visited[start] = True
    cnt = 1

    while q:
        cur = q.popleft()
        # 현재 학생이 선택한 학생 
        link = nums[cur]

        # 사이클 성사 
        # 자기 자신과 사이클  
        if cur == link:
            visited[cur] = True
            # 사이클 탐색 종료
            return 1
        
        # 일반적인 사이클이라면 
        elif start == link:
            return cnt
        
        # link가 route 안에 있다면 
        elif link in route:
            '''
            (반례에 대응)
            1 
            4
            2 3 4 2
            '''
            # link부터 끝까지의 경로 길이 
            i = route[link]
            l = len(route) - (i)
            return l
        
        if not visited[link]:
            q.append(link)
            visited[link] = True
            route[link] = len(route)
            cnt += 1

    return 0 
        
T = int(input())

for test_case in range(T):
    # 학생 넘버 1 ~ N+1
    N = int(input())
    nums = list(map(int, input().split()))
    # 학생넘버 1부터 시작하기 위해 0번 인덱스 추가 
    nums.insert(0, 0)
    # 사이클 성사된 애들 체크하는 리스트 
    visited = [False] * (N + 1)
    total = 0

    for i in range(1, N+1):
        if not visited[i]:
            total += bfs(i)

    print(N - total)
