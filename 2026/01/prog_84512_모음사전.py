# 완탐
# 중복조합 
answer = -1
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    def recur(sel):
        global answer 
        answer += 1

        if sel == word:
            return True
        
        # 기저 조건 
        if len(sel) == 5:
            return False
        
        for i in range(len(alpha)):
            sel += alpha[i]
            if recur(sel): return True
            sel = sel[:-1]
            
    recur('')
    
    return answer