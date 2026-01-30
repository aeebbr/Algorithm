import string
def solution(msg):
    answer = []
    dic = {}
    
    # 알파벳을 사전에 초기 세팅 
    for i in range(26):
        alpha = string.ascii_uppercase[i]
        dic[alpha] = i + 1
        
    left = 0
    limit = len(msg)
    
    while left < limit:
        word = msg[left]
        right = left + 1
        
        # 사전에서 문자열 찾기 
        while right < limit and (word + msg[right]) in dic:
            word += msg[right]
            right += 1
        
        # word 출력 
        answer.append(dic[word])
        
        # 사전에 문자열 추가하기 
        if right < limit:
            dic[word + msg[right]] = len(dic) + 1
        
        left += len(word)
            
    return answer