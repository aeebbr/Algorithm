'''
*** 숫자를 조합하는 것이 아니라, 부호를 조합하는 것임! 
선택지는 + 혹은 - 
'''
answer = 0
def solution(numbers, target):
    def dfs(num, idx):
        global answer
        if idx == len(numbers):
            if num == target:
                answer += 1
            return 

        dfs(num+numbers[idx], idx+1)
        dfs(num-numbers[idx], idx+1)
            
    dfs(0, 0)
    return answer