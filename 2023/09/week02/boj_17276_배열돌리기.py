import sys 
input = sys.stdin.readline
import copy

T = int(input())

for test_case in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mid = (n+1) // 2 - 1
    # 총 회전 수 
    round = d // 45

    # 각도 구분 
    # 시계 방향
    if d > 0:
        for _ in range(round):
            copy_arr = copy.deepcopy(arr)
            for i in range(n):
                # 주대각선 
                copy_arr[i][mid] = arr[i][i]
                # 가운데 열 
                copy_arr[i][n-i-1] = arr[i][mid]        
                # 부대각선
                copy_arr[mid][n-i-1] = arr[i][n-i-1]
                # 가운데 행
                copy_arr[i][i] = arr[mid][i]

            # 회전 1회 끝 
            arr = copy.deepcopy(copy_arr)

    # 반시계 방향 
    else:
        for _ in range(-1*round):
            copy_arr = copy.deepcopy(arr)
            for i in range(n):
                # 주대각선 
                copy_arr[mid][i] = arr[i][i]
                # 가운데 열 
                copy_arr[i][i] = arr[i][mid]        
                # 부대각선
                copy_arr[i][mid] = arr[i][n-i-1]
                # 가운데 행
                copy_arr[n-i-1][i] = arr[mid][i]

            # 회전 1회 끝 
            arr = copy.deepcopy(copy_arr)
            
    for row in arr:
        print(*row)
