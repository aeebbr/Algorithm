import sys 
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())

# idx: 넣고있는 숫자가 배열에서 몇 번째 인덱스인지  
def recur(idx, visited, sel):
    # 종료 조건
    # 길이가 M일 때 
    if idx == M:
        print(*sel)
        return 
    
    for next in range(0, N):
        if not visited[next + 1]:
            sel[idx] = next + 1
            visited[next + 1] = True

            recur(idx + 1, visited, sel)
            visited[next + 1] = False

sel = [0] * (M)
visited = [False] * (N + 1)

recur(0, visited, sel)