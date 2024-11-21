def solution(clothes):
    answer = 1
    dic = {}
    
    for i, j in clothes:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 2
            
    for v in dic.values():
        answer *= v
    
    return answer - 1