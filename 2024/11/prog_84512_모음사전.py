answer = 0

def solution(word):
    moeum = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(sel):
        global answer
        
        if sel:
            answer += 1
        if ("").join(sel) == word:
            return True
        if len(sel) == 5:
            return False
        
        for i in range(len(moeum)):
            sel.append(moeum[i])
            if dfs(sel):
                return True
            sel.pop()
    
    dfs([])
    
    return answer