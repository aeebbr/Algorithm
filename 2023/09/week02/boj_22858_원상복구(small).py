'''
(P:카드) 1, 4, 5, 3, 2
(D:수열) 4, 3, 1, 2, 5
=> 4번째 카드인 3을 1번째로 
    1. d: 4, D에서 1번째  
    2. P에서 d번째 카드를 1번째로 
=> 3번째 카드인 5를 2번째로 
결과: 3, 5, 1, 4, 2

되돌리기
결과에서 1번째 카드: 3
    D에서 1번째 카드: 4
    => 결과의 3은 원본에서 4번째 자리 
결과에서 2번째 카드: 5
    D에서 5번재 카드: 2
    => 결과의 5는 원본에서 2번째 자리 

로직 
1. N번 반복하며 
    2. 결과에서 N번째 카드 찾고 
    3. D에서 N번째 카드 찾기 
    4. 2의 수를 3의 자리에 놓기 
'''
import sys
input = sys.stdin.readline
import copy

N, K = map(int, input().split())
# 모든 셔플 후 결과 
S = list(map(int, input().split()))
# 수열
D = list(map(int, input().split()))

S.insert(0, 0)
D.insert(0, 0)

answer = [0] * (N+1)
for i in range(K):
    # 각 숫자 순회 
    for j in range(1, (N+1)):
        s = S[j]
        d = D[j]

        answer[d] = s
    S = copy.deepcopy(answer)

del answer[0]
print(*answer)

