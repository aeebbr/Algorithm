'''
- 악보의 길이 = 음악의 길이 

0. #이 붙은 것과 안 붙은 것을 구분할 것: 
    - 실제 재생 부분과 m 비교할 때는 앞에도 #을 붙여서 m과 재생음 비교하기 
1. 재생 시간과 음악 길이를 비교해서 실제 재생 부분을 얻기 
2. 실제 재생 부분 안에 m이 포함되는지 확인 
'''
def solution(m, musicinfos):
    '''
    #이 붙는 음을 구분 
    [C, C, #, B, C] 라면 [C, #C#, B, C] 로 변환
    '''
    def seperate_sharp(arr):
        stack = []
        
        for i in range(len(arr)):
            cur = arr[i]
            
            if cur == '#':
                stack[-1] = '#' + stack[-1]
                stack[-1] += '#'
            else:
                stack.append(cur)
        return stack
    
    def cal_play_time(start, end):
        start_h, start_m = list(map(int, start.split(":")))
        end_h, end_m = list(map(int, end.split(":")))
        start_to_min = start_h*60 + start_m
        end_to_min = end_h*60 + end_m
        
        return end_to_min - start_to_min
        
    def cal_play_melody(melody):
        play_melody = []
        cnt = 0
        
        while True:
            for m in melody:
                if cnt == play_time:
                    flag = True
                    return "".join(play_melody) 
                
                play_melody.append(m)
                cnt += 1
        return 
    
    answer = []
    
    # m 샵 구분
    m = "".join(seperate_sharp(list(m)))
    
    for i in range(len(musicinfos)):
        start, end, title, origin = musicinfos[i].split(",")
        
        # 원본 악보 샵 구분 
        origin = seperate_sharp(origin)

        # 음악 시간 계산 
        play_time = cal_play_time(start, end)
        
        # 재생 음 구하기 
        play_melody = cal_play_melody(origin)
        
        # 재생 음악 안에 m이 포함되는지 확인 
        if m in play_melody:
            answer.append((play_time, i, title)) # 재생 시간, 인덱스, 음악 제목 
        
    # answer 정렬 
        # 1. 재생시간 내림차순, 인덱스 오름차순 
    answer = sorted(answer, key = lambda x:[-x[0], x[1]])
    
    if answer:
        return answer[0][-1] # 음악제목 반환
    else:
        return "(None)"