def solution(s):
    answer = ''
    is_new_word = False
    
    for alp in s:
        if alp == " ":
            answer += alp
            is_new_word = False
        else:
#           첫 문자인 경우: is_new_word가 False임 -> True로 변환 
#           첫 문자가 아닌 경우: is_new_word가 True임 -> False로 변환 

#           첫 문자 아님 
            if is_new_word:
                answer += alp.lower()
#           첫 문자 -> 문자 시작 표시 
            else: 
                answer += alp.upper()
                is_new_word = True
                
    return answer