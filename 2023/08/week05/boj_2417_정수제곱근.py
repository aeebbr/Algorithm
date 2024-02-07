N = int(input())

# 이분 탐색
low = 0
high = N

# 제곱이 N과 같거나, N보다 커야함
# N보다 크다면 그 중 가장 작은 값이어야 함
while low <= high:
    min = (low + high) // 2

    # min의 제곱과 N 비교 
    if min**2 > N or min**2 == N: # N보다 크거나 같음 
        # 범위 낮추기 
        high = min - 1
    elif min**2 < N: # N보다 작음
        # 범위 높이기 
        low = min + 1

print(low)