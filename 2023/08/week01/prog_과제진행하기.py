def solution(plans):
    answer = []
    # 스택
    waiting = []
    
    # 시작 시간을 분으로 변환
    for i in range(len(plans)):
        start = plans[i][1]
        h = int(start[:2])
        m = int(start[3:])
        time = h * 60 + m
        plans[i][1] = time
        plans[i][2] = int(plans[i][2])
        
    # 시작 시간을 기준으로 정렬
    plans.sort(key = lambda x: x[1])
        
    # 현 과제가 없어질 때까지 탐색 => 현 과제를 모두 탐색 => for 문으로 현 과제 반복
    # 대기열에 과제가 없어질 때까지 탐색 => while 문으로 대기열 반복 
    for i in range(len(plans)):
        # 현 과제 
        cur_name, cur_start, cur_time = plans[i]
        cur_end = cur_start + cur_time
                
        # 현 과제가 마지막 과제라면 도중에 끼어들 다음 과제가 없으므로 이 과제는 무조건 이번 턴에 종료됨
        if i == len(plans) - 1:
            # 현 과제 종료 
            answer.append(cur_name)
            # 탐색 종료 
            break
            
        # 다음 과제 
        next_name, next_start, next_time = plans[i + 1]        
        
        # 현 과제 종료 시간 전에 다음 과제 시작 시간이 된다면 
        if cur_end > next_start: 
            # 현 과제 중단
            # 현 과제 남은 시간 갱신
            # 종료 시간 - 중단 시간(다음 과제 시작)
            plans[i][2] = cur_end - next_start
            # 현 과제를 대기열로 
            waiting.append(plans[i])
            
            # 다음 과제 시작
        # 현 과제 종료 후에 다음 과제 시작이라면 
        else:
            # 현 과제 종료 
            answer.append(cur_name)            
            
            # 종료와 동시에 시작할 다음 과제가 없다면
            if cur_end != next_start:
                # 다음 과제 시작 시간이 될 때까지 대기 과제 수행
                # 대기 과제가 있다면 
                while waiting:
                    # 대기 과제 시작
                    wait_name, wait_start, wait_time = waiting.pop()
                                        
                    # 대기 과제가 중단되어야 하는지 확인
                    # 대기 과제 종료 전에 다음 과제가 시작하는가? 
                    # 대기 과제 종료 시간: 현 과제 종료 + 대기 과제 시간
                    if cur_end + wait_time > next_start:
                        # 대기 과제 중단, 다음 과제 시작 
                        # 대기 과제 남은 시간 갱신
                        # 대기 과제 종료 시간 - 중단 시간(다음 과제 시작)
                        wait_time = (cur_end + wait_time) - next_start
                        # 대기 과제 다시 대기열로 
                        waiting.append([wait_name, wait_start, wait_time])
                        
                        # 다음 과제로 
                        break
                    # 대기 과제 종료 
                    else:
                        answer.append(wait_name) 
                        
                        # 현재 종료 시간 갱신
                        cur_end = cur_end + wait_time
            
    # 대기 과제가 남아있다면 최근에 멈춘 과제부터 시작, 종료 
    while waiting:
        wait_name = waiting.pop()[0]
        answer.append(wait_name)
    
    return answer