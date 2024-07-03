def solution(keymap, targets):
    answer = []
    
    dic = {}
    for key in keymap:
        for i in range(len(key)):
            cur = key[i]
            if (cur in dic and i + 1 < dic[cur]) or cur not in dic: 
                    dic[cur] = i + 1
    
    # 자판 누르기
    for target in targets:
        total = 0
        for t in target:
            if t in dic:
                total += dic[t]
            else:
                answer.append(-1)
                break
        else:
            answer.append(total)
    
    return answer