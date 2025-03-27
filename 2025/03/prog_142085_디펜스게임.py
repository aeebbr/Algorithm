'''
매 라운드마다 병사 소진, 이 때 각 병사의 수를 최대힙에 저장 
병사가 부족할 때 최대힙의 가장 맨앞(소진이 가장 큰 병사 수)를 pop해서 현재의 병사 수에 보태기 
=> 무족권을 쓴 셈이 됨 
'''
import heapq
def solution(n, k, enemy):
    answer = 0
    max_heap = []
    heapq.heapify(max_heap)
    
    for e in enemy:
        # 병사 소진 
        n -= e
        # 힙에 소진한 병사 수 삽입 
        heapq.heappush(max_heap, (-e, e))
        
        # 병사를 소진한 후에 남은 병사가 음수라면 => 병사를 소진했던 시점에 병사가 부족했던 것 
        # 만약 n이 3, e가 4였다면 병사가 부족함 => n은 -1이 됨 
        # 만약 n이 3, e가 2였다면 병사가 충분함 => n은 1이 됨 
        if n < 0:
            # 무족권이 남아있다면 
            if k > 0:
                _, max_army = heapq.heappop(max_heap)
                n += max_army
                k -= 1
            # 무족권이 안 남아있으면 패배, 게임 끝 
            else:
                break
        
        answer += 1
    
    return answer