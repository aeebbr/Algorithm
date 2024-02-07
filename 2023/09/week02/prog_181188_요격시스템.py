# 이전 종료와 현재 시작 비교 
    # 이전 종료 > 현재 시작 => 겹치는 구간 

def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x:[x[1], x[0]])
    
    pre_end = 0
    for s, e in targets:
        # 요격할 수 없을 때 카운트 
        if pre_end <= s:
            answer += 1
            # 이전 종료 지점 갱신 
            pre_end = e
            
    
    return answer