answer = 0
def solution(numbers, target):    
    def dfs(number, idx):
        global answer 
        if idx == len(numbers):
            if number == target: # 성공 
                answer += 1
            return

        tmp = numbers[idx]
        dfs(number + tmp, idx+1)
        dfs(number - tmp, idx+1)
    
    dfs(0, 0)
    
    return answer