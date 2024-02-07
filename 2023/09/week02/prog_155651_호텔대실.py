# 종료 시간 + 10분 더해서 생각하기 
# 시간 + 분을 분으로 바꾸기 

# 한 행에 들어갈 수 없는 경우 
    # 이전 종료 전에 현재 시작하는 경우 

# 모든 예약 시간 순회하면서, 현재 시간 뒤에 올 수 있는 시간 찾고, 없으면 다음 행으로 넘어가기 
def solution(book_time):
    answer = 1
    
    # 분 변환
    for i in range(len(book_time)):
        start, end = book_time[i]
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))
        
        start = start_hour * 60 + start_minute
        end = end_hour * 60 + end_minute + 10 # 청소시간 10분 추가 
        
        book_time[i] = [start, end]
            
    book_time.sort()
    
    cur_idx = 0
    for _ in range(len(book_time)-1):
        end = book_time[cur_idx][1]
        del book_time[cur_idx]

        # 현재 종료 이후에 시작이 있는 경우를 찾기 (시작 빠른 것부터)
        for j in range(len(book_time)):
            ns = book_time[j][0]
            if ns >= end:
                # 이전 종료 시간 갱신
                cur_idx = j
                # 가능한 방 있다면 다음 턴에서 pop될 것 
                break
        # 가능한 것 없다면 다음 방으로 
        else:
            # 남은 시간 중 시작 시간 가장 빠른 것으로 
            cur_idx = 0 
            answer += 1
    
    return answer