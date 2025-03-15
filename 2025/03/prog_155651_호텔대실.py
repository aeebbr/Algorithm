'''
정렬 기준
    1. 시작을 기준으로 정렬
    2. 종료를 기준으로 정렬 

청소시간까지 포함한 종료시간을 최소힙에 삽입 
최소힙의 각 원소는 방을 의미 
최소힙의 front는 종료가 가장 빠른 방을 의미 
현재 예약 시간이 front의 종료보다 전이라면 최소힙에 현재를 삽입하여 방 추가, 후라면 front 빼고 현재를 삽입 
    => 어느 경우에든 간에 현재 예약은 최소힙에 항상 삽입됨
'''
import heapq
def solution(book_time):
    answer = 0
    book_time = sorted(book_time, key = lambda x: (x[0], x[1]))
    room_q = []
    
    for s, e in book_time:
        s_h, s_m = list(map(int, s.split(":")))
        e_h, e_m = list(map(int, e.split(":")))
        s_total = s_h*60+s_m
        e_total = e_h*60+e_m+10 # # 청소시간 10분 포함
        
        if room_q:
            # 방에 있는 예약 중 가장 빠른 종료 시간  
            pre_e_total = heapq.heappop(room_q) 

            # 현재의 시작이 pre_e_total보다 작다면 pre_e_total 다시 삽입 = pre_e_total를 그대로 남김으로써 현재를 새로운 방에 추가하는 것  
            if s_total < pre_e_total:
                heapq.heappush(room_q, pre_e_total)
        
        # 현재 예약 넣기 
        heapq.heappush(room_q, e_total)
        
#         # 현재의 시작이 가장 빨리 끝나는 방보다 크거나 같다면 해당 방의 다음 순서로 스케줄링
#         if room_q and s_total >= room_q[0]:
#             heapq.heappop(room_q)
        
#         # 현재 예약 넣기 
#         heapq.heappush(room_q, e_total)
        
    return len(room_q)