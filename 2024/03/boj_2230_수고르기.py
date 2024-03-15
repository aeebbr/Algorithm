import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
answer = float("inf") # 최소값
arr.sort()

end = 0 # end 포인터 

for start in range(N): # start 포인터 
    # end가 범위를 벗어나거나, 차이가 M 이상이면 탈출 
    while end < N and arr[end]-arr[start] < M:
        end += 1

    # end가 범위를 벗어났다면 종료 
    if end >= N:
        break

    # 차이가 M이면 여기에서 탈출해야 함 => 차이와 M 비교를 여기에서 해야 함
    tmp = arr[end] - arr[start]
    # 차이가 M이면 더 이상 진행할 필요 없음, 종료 
    if tmp == M:
        answer = M
        break
    # 차이가 M 이상이니까 갱신
    answer = min(answer, tmp)

print(answer)
