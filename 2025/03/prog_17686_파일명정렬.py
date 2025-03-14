def solution(files):
    answer = []
    sorted_files = [] # [(헤드, 숫자, 전체 파일명), ... ]
    
    # files의 각 파일명 쪼개기 
    for file in files:
        num_start, num_end = 0, 0
        
        for j in range(len(file)):
            # 숫자라면 
            if file[j].isdigit():
                # 시작 설정이 안 돼있다면 
                if num_start == 0:
                    num_start = j
                # 시작 설정이 돼있다면 끝 설정 
                else:
                    num_end = j
            # 숫자가 아니라면 
            else:
                # 숫자가 아닌데, 숫자가 이미 있었다면 => 숫자 구간 끝 
                if num_start != 0:
                    break
                    
        if num_end == 0: # number가 한 글자인 경우 대비 
            num_end = num_start
            
        # 숫자를 기준으로 쪼개기 
        head = file[:num_start]
        number = file[num_start: num_end+1]
        
        sorted_files.append((head, number, file))
                    
    sorted_files = sorted(sorted_files, key = lambda x: [x[0].lower(), int(x[1])])
    
    for h, n, f in sorted_files:
        answer.append(f)
        
    return answer