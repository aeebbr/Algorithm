def solution(m, musicinfos):
    '''
    #이 붙는 음을 구분 
    [C, C, #, B, C] 라면, [C, #C#, B, C] 로 변환
    '''
    def separate_sharp(arr):
        stack = []
        for j in range(len(arr)):
            cur = arr[j]
            if cur == '#':
                stack[-1] = '#' + stack[-1]
                stack[-1] += '#'
            else:
                stack.append(cur)
        return stack
    
    def cal_play_time():
        # 시작과 종료 시간을 분 단위로 변환 
        start_hour, start_min = map(int, start_time.split(":"))
        end_hour, end_min = map(int, end_time.split(":"))
        start_to_min = start_hour * 60 + start_min
        end_to_min = end_hour * 60 + end_min

        # 음악 재생 시간 = 종료 시간 - 시작 시간
        return end_to_min - start_to_min
    
    def cal_play_melody(melody):
        play_melody = []
        cnt = 0 # 재생된 음의 개수 
        
        while True:
            for s in melody:
                if cnt == play_time:
                    return (" ").join(play_melody)
                play_melody.append(s)
                cnt += 1
        
    answer = []
    # m의 샵 구분 
    m = (" ").join(separate_sharp(list(m)))
    
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(",") # 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
        # 악보의 샵 구분
        melody = separate_sharp(list(melody)) 
        # 음악 재생 시간 계산 
        play_time = cal_play_time() 
        # 재생 시간동안 재생된 음 저장 
        play_melody = cal_play_melody(melody)
        
        # 찾고있는 음이 재생된 것 안에 있는지 확인 
        if m in play_melody:
            # (재생 시간, 음악이 입력된 순서, 제목)
            answer.append((play_time, len(answer), title)) 
            
    # 조건 같은 음악이 여러 개라면 <1. 재생 시간 내림차순, 2. 음악 입력 순서 오름차순> 정렬
    answer = sorted(answer, key = lambda x:[-x[0], x[1]])

    if answer:
        # 정렬 결과 가장 앞순서인 음악의 제목 반환 
        return answer[0][2] 
    else:
        return "(None)"