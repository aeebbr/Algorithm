# 재귀 
# 분기는 +와 -
import sys
# sys.setrecursionlimit(90000)
answer = 0
def solution(numbers, target):
    def recur(idx, total, sel):
        global answer
        # 기저 조건
        if idx == len(numbers):
            if total == target:
                answer += 1
            return 
    
        sel.append(numbers[idx])
        recur(idx+1, total+numbers[idx], sel)
        sel.pop()
        
        sel.append(-numbers[idx])
        recur(idx+1, total-numbers[idx], sel)
        sel.pop()
            
    recur(0, 0, [])

    return answer