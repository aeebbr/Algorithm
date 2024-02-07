import heapq
def solution(n, k, enemy):
    sum_enemy = 0
    heap = []
    
    # 각 라운드 순회 
    for i in range(len(enemy)):
        # 이번 라운드 적 수 누적
        sum_enemy += enemy[i]
        # 이번 라운드 적 수 힙에 삽입 
        # 내림차순 정렬 위하여 음수로 삽입
        heapq.heappush(heap, -enemy[i])
        
        # 지금까지의 적 수가 병사 수보다 많다면 
        if sum_enemy > n:
            # 남은 무적권 기회가 없다면 실패 
            if k <= 0:
                # 라운드 리턴 
                return i
            
            # 무적권 사용
            k -= 1
            # 지금까지의 라운드 중 가장 많은 적이 있던 라운드의 적 수를 차감 
            # 힙 내부는 음수이기 때문에 더하기 연산 
            sum_enemy += heapq.heappop(heap)
    
    # 모든 라운드를 방어 
    return len(enemy)