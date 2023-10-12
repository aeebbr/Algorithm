def solution(name, yearning, photo):
    answer = []
    
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for p in photo:
        sum = 0
        for i in p:
            if i in dic:
                sum += dic[i]
        answer.append(sum)
    
    return answer