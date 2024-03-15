'''
5 10
1 2 3 4 5
'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# S 이상이면 start 증가  
# S 미만이면 end 증가 

end = 0
answer = float("inf") # 최소값
total = arr[0]

for start in range(N):
    # 현재 start를 기준으로 end를 증가시켜야 
    # end가 범위를 벗어나면 종료 
    while end < N and total < S:
        end += 1
        if end != N:
            total += arr[end]

    if end >= N:
        break

    # 다음 start로 이동 
    total -= arr[start]
    # 길이 갱신 
    answer = min(answer, end-start+1)

if answer == float("inf"):
    print(0)
else:
    print(answer)
