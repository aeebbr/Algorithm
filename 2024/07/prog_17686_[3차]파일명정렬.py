def solution(files):
    answer = []
    
    # 1. 헤드 사전순 / 2. 숫자 순 => [(헤드, 숫자, 파일명)]
    sort_standard = []
    
    for file in files:
        # 넘버 인덱스 범위를 찾기 
        num_idx_start, num_idx_end = 0, len(file)-1 # 테일이 없어서 num_idx_end가 계산 안될 경우를 대비해서 초기화를 마지막 인덱스로 
        
        for i in range(len(file)):
            f = file[i]
            if f.isdigit():
                # 넘버 구간 시작 
                if num_idx_start == 0:
                    num_idx_start = i
            else:
                # 넘버 구간 끝
                if num_idx_start != 0:
                    num_idx_end = i-1
                    break
                    
        # 헤드 
        head = file[:num_idx_start]
        # 넘버 
        number = file[num_idx_start:num_idx_end+1]
        # 헤드를 소문자로 변환
        head = head.lower()
        # 숫자형으로 변환 
        number = int(number)
        
        sort_standard.append((head, number, file))
        
    # 정렬 
    sort_standard = sorted(sort_standard, key = lambda x: [x[0], x[1]])
    
    for h, n, f in sort_standard:
        answer.append(f)
    
    return answer