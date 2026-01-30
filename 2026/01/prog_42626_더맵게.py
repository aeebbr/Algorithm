# 최소힙 
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    # 힙에 원소 하나 남을 때까지 
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        tmp = a + (b*2)
        heapq.heappush(scoville, tmp)
        answer += 1
        
    if scoville[0] >= K:
        return answer 
    else:
        return -1