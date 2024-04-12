import heapq
def solution(jobs):
    answer = 0
    q = []

    # 현재 시간 
    cur_time = 0
    # 수행한 작업 개수 
    cnt = 0
    # 이전 작업의 시작 시점
    start_time = -1
    
    # 모든 작업이 끝나면 종료 
    while cnt < len(jobs):
        # 1. 남은 것들 중 
        # 2. 현재 시점을 기준으로 당장 시작할 수 있는 것
        # 3. 중에서 소요 시간이 가장 짧은 것 선택
        
        # 고려할 것: 남은 작업들을 어디에 저장? 
            # 최소 소요 시간을 바로 뽑을 수 있는 자료구조가 적합 => 최소힙
            # 현재 시점 > 요청 시점 > 이전작업의 시작 시점인 작업이라면 힙에 넣기 

        for j in jobs:
            if cur_time >= j[0] > start_time:
                heapq.heappush(q, (j[1], j[0])) # 소요시간 기준으로 최소힙

        # 수행할 수 있는 작업이 있다면
        if q:
            # 작업 수행하기 전에 시작 시점 갱신하기 
            start_time = cur_time
            # 현재 작업(=소요시간이 가장 짧은) 수행하기 
            running_time, req_time = heapq.heappop(q)
            # 수행이 끝난 현재 시간 갱신하기 
            cur_time += running_time

            # 현재 작업의 총 시간 누적
                # 현재시간 - 작업의요청시간
            answer += cur_time - req_time
            cnt += 1
        # 수행할 수 있는 작업이 없다면
        else:
            cur_time += 1
            
    return answer // len(jobs)

'''
# 솔루션 
from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    num = len(jobs)
    waiting = [] 
    count = [] 
    now = 0 

    while len(count) != num : 
        while jobs and now >= jobs[0][0] : 
            top = jobs.pop(0)
            heappush(waiting, (top[1], top[0]))

        if jobs and waiting == []:
            top = jobs.pop(0)
            now = top[0]
            heappush(waiting, (top[1], top[0]))
  

        x,y = heappop(waiting)
        now += x 
        count.append(now-y)

    return sum(count)//num'''