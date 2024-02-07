import sys
input = sys.stdin.readline

N = int(input())
circles = []

for i in range(N):
    x, r = map(int, input().split())

    # 왼 좌표 
    left = x - r
    # 오른 좌표 
    right = x + r

    # (좌표, 인덱스, 왼/오)
    circles.append((left, i, 'l'))
    circles.append((right, i, 'r'))

# 좌표 기준으로 오름차순 정렬
circles.sort()

stack = []

# circles 순회 
for i in range(len(circles)):
    if circles[i][2] == 'l':
        stack.append(circles[i])
    else:
        left = stack.pop()

        if left[1] != circles[i][1]:
            print("NO")
            break
else:
    print("YES")
