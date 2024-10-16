def solution(s):
    answer = ''    
    arr = s.split(" ")
    
    for a in arr:
        if a == "":
            answer += " "
            continue
            
        first = a[0]
        other = a[1:].lower()
        if a[0].isalpha():
            first = first.upper()
        
        answer += first + other + " "
    
    return answer[:-1]