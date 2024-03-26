def solution(genres, plays):
    answer = []
    dic = {}
    
    for i, g, p in zip(range(len(plays)),genres, plays):
        if g in dic:
            dic[g][0] += p
            dic[g][1].append([p, -i])
        else:
            dic[g] = [p, [[p, -i]]]
                
    '''
    장르: [총 횟수, [[횟수, 번호], [횟수, 번호]]]
    1. 총 횟수 기준으로 내림차순 정렬, 
    2. 횟수 기준으로 내림차순 정렬, 
    3. 번호 기준으로 오름차순 정렬 
    '''
    
    # dic 정렬 
    dic = sorted(dic.items(), key = lambda x:x[1][0], reverse = True)
    
    for i, j in dic:
        tmp = sorted(j[1], key = lambda x:(x[0], x[1]), reverse=True)
        for k in range(0, min(2, len(tmp))):
            answer.append(-tmp[k][1])
    
    return answer