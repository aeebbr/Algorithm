import heapq
answer = []
heapq.heapify(answer)
def solution(storey):
    def dfs(total, cnt):
        global answer
        # 기저조건: total이 0이면 종료 
        if total == 0:
            heapq.heappush(answer, cnt)
            return 
        
        '''
        324 // 10 = 32(10을 32번 빼기해야 일의 자리가 없어짐)
        324 % 10 = 4(10을 32번 빼기해서 제거된 일의 자리는 4임)
            10씩 빼기를 해야할까 10씩 더하기를 해야할까?: 
                => 남은 일의 자리를 모두 1씩 빼서 0으로 만드는 게 빠른지, 일의 자리를 1씩 더해서 10으로 만든 후 모두 10씩 빼는 게 빠른지 판별하면 됨 
            up: 10 - 4 = 6(일의 자리가 10이 되려면 +1을 6회)
            down: 4(일의 자리가 0이 되려면 -1을 4회)
            => down하는 게 더 빠름 
            
        16 % 10 = 6(10을 1번 빼기해서 제거된 일의 자리는 6임)
            up: 10 - 6 = 4(일의 자리가 10이 되려먼 +1을 4회)
            down: 6(일의 자리가 0이 되려먼 -1을 6회)
            => up하는 게 더 빠름 
        '''
        
        one = total % 10 # 일의 자리 
        up =  10 - one # 일의 자리가 10이 되려면 +1을 몇 회해야 하는지  
        down = one # 일의 자리가 0이 되려면 -1을 몇 회해야 하는지 
        
        # up과 down 중 더 적은 쪽으로 이동 
        # 일의 자리를 0이나 10으로 만들어 버리고, 그 일의 자리는 아예 버리기
        if up < down: # up하기 
            # 1. 16 -> 20(+1을 4회)
            # 2. 20 -> 2(일의 자리가 0이 됐으니 버리고, 십의 자리가 일의 자리가 됨)
            dfs(total // 10 + 1, cnt + up) # 16 // 10 = 1 + 1 = 2, 
        elif up > down: # down하기 
            # 일의 자리를 0으로 모두 제거 
            # 1. 324 -> 320(-1을 4회) 
            # 2. 320 -> 32(일의 자리가 0이 됐으니 버리고, 십의 자리가 일의 자리가 됨 )
            dfs(total // 10, cnt + down) # 324 // 10 = 32
        else:
            # up, down 횟수 같다면 둘 다 
            for i in range(2):
                dfs(total // 10 + i, cnt + up)  
            
    dfs(storey, 0)
    
    # 최소힙 안의 가장 적은 수(가장 적은 카운트)가 답
    return heapq.heappop(answer) 