# 이분 탐색
import sys 
inpurt = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# 이분 탐색을 위하여 오름차순 정렬 
cards.sort()

for n in nums:
    # cards의 첫 인덱스, 마지막 인덱스 
    low, high = 0, N - 1
    flag = False

    # low 인덱스가 high 인덱스를 넘지 않아야 함
    while low <= high:
        # cards의 중간 인덱스 
        mid = (low + high) // 2

        # 찾아야 하는 수와 카드의 중간값을 비교하여 찾는 범위를 설정해감
        if n < cards[mid]:
            # 중간값보다 작다면 범위를 중간값보다 작게 설정
            # high를 중간값 이전까지 
            high = mid - 1
        elif n > cards[mid]:
            # 중간값보다 크다면 범위를 중간값보다 크게 설정
            # low를 중간값 다음까지 
            low = mid + 1
        else:
            # 수 찾음(중간값이 n임)
            flag = True
            break

    if flag:
        print(1, end=" ")
    else:
        print(0, end=" ")

# 딕셔너리 풀이 방법(성공)
# import sys 
# inpurt = sys.stdin.readline

# N = int(input())
# cards = list(map(int, input().split()))
# M = int(input())
# nums = list(map(int, input().split()))

# cards_dic = {}
# for i in range(N):
#     cards_dic[cards[i]] = 0

# for n in nums:
#     if n in cards_dic:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")