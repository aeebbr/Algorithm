def solution(input_string):
    answer = []
    # alpha = list(set(input_string))
    dic = {}
    
    for i in range(len(input_string)):
        alpha = input_string[i]
        if not alpha in answer:
            if alpha in dic:
                # 이미 있다면 그 인덱스가 내 이전 인덱스인지 확인 
                pre = dic[alpha]
                if pre == i - 1:
                    # 맞다면 갱신 
                    dic[alpha] = i
                else:
                    answer.append(alpha)
            else:
                dic[alpha] = i
     
    answer.sort()
    result = ''
    for j in answer:
        result += j
            
    if result == "":
        return 'N'
    else:
        return result