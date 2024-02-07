import sys 
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
# 비교군
# [인덱스, 높이]
stack = []
# 각 탑의 수신탑 저장
answer = [0] * N

# 모든 탑 순회하면서 비교탑과 비교 
for i in range(len(top)):
    # 비교군 순회하면서 비교 
    while stack:
        # 비교탑이 현재탑보다 높다면 수신
        if top[i] < stack[-1][1]:
            # 비교탑을 현재탑의 수신탑으로 저장
            answer[i] = stack[-1][0] + 1

            # 수신탑 찾았으니 다음 탑의 수신탑 찾으러 
            break
        # 수신 불가 
        # 현재탑이 더 높기 때문에 비교탑은 그 뒤의 다른 탑들의 수신탑도 될 수 없음
        else:
            # 비교탑을 비교군에서 제거 
            stack.pop()
    
    # 현재탑을 비교군에 추가 
    stack.append([i, top[i]])

print(*answer)