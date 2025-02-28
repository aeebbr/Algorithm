'''
사전순 중복조합 
'''
answer = -1
def solution(word):
    def combi(arr):
        global answer 
        
        # 기저조건 
        if len(arr) > 5:
            return False
        
        answer += 1
        if arr == target:
            return True
        
        for i in range(len(alpha)):
            arr.append(alpha[i])
            if combi(arr):
                return True
            arr.pop()
            
        return False
    
    alpha = ['A', 'E', 'I', 'O', 'U']
    target = list(word)
    combi([])
    
    return answer