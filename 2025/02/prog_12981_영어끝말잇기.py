def solution(n, words):
    '''
    1. 틀린 단어 찾기
        - 중복 어떻게?: 전체에서 중복 찾지 말고, dict 형태로, 시작하는 문자 기준으로 분류
    3. 그 단어의 위치(인덱스 번호) 기반으로 답 계산 
    '''
    answer = []
    first_word = words[0]
    dic = {first_word[0]: [first_word]}
    pre_end = first_word[-1] # 첫 단어로 초기화 
    idx = 0
    
    for i in range(1, len(words)):
        cur = words[i]
        cur_start = cur[0]
        
        # 중복 확인 
        if cur_start in dic:
            # 중복임, 탈락 
            if cur in dic[cur_start]:
                idx = i
                break
            else:
                dic[cur_start].append(cur)
        else:
            dic[cur_start] = [cur]
                
        # 중복 검사 통과함 
        # 이전 문자열과 이어지는지 확인 
        # 이어지지 않음, 탈락
        if cur_start != pre_end:
            idx = i
            break
            
        pre_end = cur[-1]
    
    # 번호, 차례 찾기 
    if idx != 0:
        '''
        3명, 8번 단어라면 
        (8+1) / 3 => 몫: 3, 나머지: 0 
        => 3번째 턴에서 탈락 
        => 3번 사람(나머지가 0이라면 마지막 사람을 의미함) 
        
        2명, 4번 단어라면
        (4+1) / 2 => 몫: 2, 나머지: 1
        => 3번째 턴에서 탈락 
        => 1번 사람
        
        3명, 7번 단어라면 
        (7+1) / 3 => 몫: 2, 나머지: 2 
        => 3번째 턴에서 탈락 
        => 2번 사람 
        '''

        i = (idx+1) // n # 몫
        j = (idx+1) % n # 나머지 
        
        if j == 0:
            answer.append(n)
            answer.append(i)
        else:
            answer.append(j)
            answer.append(i+1)
    # 탈락자 없음 
    else:
        answer.append(0)    
        answer.append(0)    
    
    return answer