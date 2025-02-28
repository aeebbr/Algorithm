# 최소힙
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1: # 배열에 원소가 적어도 2개는 남아있어야 함 
        if scoville[0] >= K:
            break
            
        tmp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, tmp)
        answer += 1
        
    else:
        if scoville[0] < K:
            answer = -1
    
    return answer