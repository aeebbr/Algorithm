# 기능 
    # 마지막 사람 -> 첫번째 사람 루프 
    # 단어 끝말잇기 확인 
    # 단어 중복 확인 
    # 한글자 단어 확인 
    # 최초 탈락자 한 명만 찾으면 끝 
import math 
def solution(n, words):
    def cal_result(i, n):
        person_num = (i+1) % n
        round_num = math.ceil((i+1)/n)
        
        return [n if person_num == 0 else person_num, round_num]
        
    pre = words[0][-1]
    dic = {words[0][0]: [words[0]]}
    
    for i in range(1, len(words)):
        cur = words[i]
        
        # 글자수 검증 -> 실패 
        if len(cur) == 1:
            return cal_result(i, n)
        
        # 끝말잇기 확인 
        # 끝말잇기 성공 
        if pre == cur[0]:
            first = cur[0]
            
            if first in dic:
                if cur in dic[first]:
                    # 중복검증 -> 실패 
                    return cal_result(i, n)
                
                dic[first].append(cur)
            else:
                dic[first] = [cur]
        # 끝말잇기 실패 
        else:
            return cal_result(i, n)
            
        pre = cur[-1]
            
    return [0, 0]