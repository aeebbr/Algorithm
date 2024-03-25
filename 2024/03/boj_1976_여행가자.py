'''
5
5
0 1 0 0 0
1 0 0 0 1
0 0 0 1 0
0 0 1 0 1
0 1 0 1 0
3 5 4 2 1

0: 1
1: 0, 4
2: 3
3: 2, 4
4: 1, 3
=> 2, 4, 3, 1, 0
'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end):
    q = deque()
    q.append((start))
    visited = [False] * N
    visited[start] = True

    while q:
        cur = q.popleft()

        if cur == end:
            return True

        for i in range(len(linked_list[cur])):
            next = linked_list[cur][i]

            if visited[next]:
                continue

            q.append((next))
            visited[next] = True

    return False

N = int(input())
M = int(input())
linked_list = []

for i in range(N):
    tmp = list(map(int, input().split()))
    linked_nodes = []
    for j in range(N):
        if tmp[j] == 1: linked_nodes.append(j)
    linked_list.append(linked_nodes)
plan = list(map(int, input().split()))

# 여행 계획 순서를 지켜야 함 
for i in range(0, len(plan)-1):
    if not bfs(plan[i]-1, plan[i+1]-1):
        print("NO")
        break 
else:
    print("YES")
