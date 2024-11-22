import heapq
# 최소힙
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        spciy_1 = heapq.heappop(scoville)
        
        if spciy_1 >= K:
            break
        if not scoville: # 실패 
            answer = -1
            break
            
        spciy_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, spciy_1 + (spciy_2 * 2))
        answer += 1
    
    return answer