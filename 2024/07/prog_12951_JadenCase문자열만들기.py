def solution(s):
    answer = ''
    
    s = s.split(" ")
    string = []
    
    for i in s:
        # 공백 문자가 아니라면
        if i:
            tmp = i[0].upper() + i[1:].lower()
        else:
            tmp = i
        string.append(tmp)
    
    answer = ' '.join(string)
    
    return answer