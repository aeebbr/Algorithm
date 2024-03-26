def solution(clothes):
    answer = 1
    dic = {}
    
    for i, j in clothes:
        if j in dic:
            dic[j].append(i)
        else:
            dic[j] = [j]
    # print(dic)
    
    # 기존 옷 * 현재 옷 + 현재 옷 개수 
    for k, v in dic.items():
        answer += answer * len(v)
    
    return answer - 1