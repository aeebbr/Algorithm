import sys
input = sys.stdin.readline
import copy

N = int(input())

score = [list(map(int, input().split())) for _ in range(3)]

sum = [0] * N
rank = []
sum_rank = []

# 회차별 등수 출력
for s in score:
    dic = {}
    rank = 0

    # 점수 오름차순 정렬
    sorted_score = copy.deepcopy(s)
    sorted_score.sort(reverse=True)

    # 등수 매기기 
    for ss in sorted_score:
        rank += 1

        # 동점자 점수 처리 
        # dic에 중복값 없어야 함 => 이미 같은 값이 있다면 해당 값은 등수 증가 안 시킴
        if ss not in dic:
            dic[ss] = rank

    # 원본 배열 순서대로 점수 저장
    arr = []
    # 정렬되지 않은 원본 배열 탐색
    for i in range(len(s)):
        # 이 점수의 등수 찾아서 삽입
        arr.append(dic[s[i]])
        # 점수 누적
        sum[i] += s[i] 
    print(*arr)

# 합산 등수 
dic = {}
rank = 0
sorted_sum = copy.deepcopy(sum)
sorted_sum.sort(reverse=True)

for s in sorted_sum:
    rank += 1
    # 동점자 처리 
    if s not in dic:
        dic[s] = rank

# 원본 순서대로 등수 저장 
arr = []
for i in range(len(sum)):
    arr.append(dic[sum[i]])

print(*arr)