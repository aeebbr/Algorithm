# M ~ N 사이의 소수 찾기
# 소수: 1과 자기 자신으로만 나누어 떨어지는 수 
M = int(input())
N = int(input())

answer = []

for num in range(M, N + 1):
    if num > 1:
        # 2 ~ num - 1의 수로 나눴을 때, 나누어 떨어지면 소수가 아님 
        for i in range(2, num):
            if num % i == 0:
                break

        # 나누어 떨어지는 수가 전혀 없었다면 소수임
        else:
            answer.append(num)

if len(answer) > 0:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)