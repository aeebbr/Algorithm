def solution(k, tangerine):
    '''
    1. 개수 내림차순 정렬
    2. 맨앞부터 선택
    3. 누적합이 k보다 크거나 같다면 종료, k보다 작다면 다음 종류로 넘어가기 
    
    2: 2
    3: 2
    5: 2
    1: 1
    4: 1
    '''
    
    answer = 0
    dic = {}
    
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    
    # 개수 내림차순 
    dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    total_cnt = 0 
    
    for size, cnt in dic:
        answer += 1
        total_cnt += cnt
        if total_cnt >= k:
            break

    return answer