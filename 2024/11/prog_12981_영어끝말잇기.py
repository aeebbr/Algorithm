def solution(n, words):
    answer = [0, 0]
    cnt = [0] * n

    # 단어의 끝나는 문자 = {끝문자: [해당단어, 해당단어 ...]}
    end_dic = {}     
    number = -1
    pre_e = '' # 이전 단어의 마지막 글자 
    is_lose = False
    
    for w in words:
        number += 1
        if number >= n:
            number = 0
        cnt[number] += 1
            
        s = w[0]
        e = w[-1]
        
        # 1. 중복 확인 
        if e in end_dic:
            if w in end_dic[e]:
                # 탈락 
                is_lose = True
                break
            end_dic[e].append(w)
        else:
            end_dic[e] = [w]
            
        # 2. 끝말 확인 
        if pre_e != '' and pre_e != s:
            # 탈락
            is_lose = True
            break
        
        pre_e = e # 이전 끝글자 갱신 
    
    if is_lose: 
        answer = [number+1, cnt[number]]
        
    return answer