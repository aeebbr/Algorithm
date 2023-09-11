# 능력치 오름차순으로 정렬 => 앞의 두 사원이 능력치 가장 작음 => 능력치 갱신 => 또 정렬 => 반복
import heapq
def solution(ability, number):
    answer = 0
    
    heapq.heapify(ability)
    
    # 교육 진행 횟수만큼 
    for i in range(number):
        first = heapq.heappop(ability)
        second = heapq.heappop(ability)
        total = first + second
        heapq.heappush(ability, total)
        heapq.heappush(ability, total)

    return sum(ability)