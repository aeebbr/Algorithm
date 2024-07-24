# 조합
answer = 0

def solution(number):
    def combi(sel, idx, total):
        global answer 
        
        if len(sel) == 3 and total == 0:
            answer += 1
            return 
            
        for i in range(idx, len(number)):
            sel.append(number[i])
            total += number[i]
            combi(sel, i+1, total)
            sel.pop()
            total -= number[i]
            
    combi([], 0, 0)
    
    return answer