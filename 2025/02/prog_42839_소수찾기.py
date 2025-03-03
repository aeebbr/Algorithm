def solution(numbers):
    def is_prime(arr):
        num = int(''.join(arr))
        
        if num <= 1:
            return False
        
        # 1과 자기자신 말고도 나뉘어지는 수가 있다면 소수가 아님 
        # 나누는 범위: 2에서부터 num-1까지 
        for i in range(2, num):
            if num % i == 0:
                return False
            
        return True
    
    def combi(arr, visited):
        # 소수 판별
        if len(arr) != 0 and is_prime(arr):
            combi_arr.append(int(''.join(arr)))
        
        # 기저조건
        if len(arr) == len(numbers):
            return 
    
        for i in range(len(numbers)):
            # 중복X
            if visited[i] == True:
                continue
            
            arr.append(numbers[i])
            visited[i] = True
            combi(arr, visited)
            arr.pop()
            visited[i] = False
        
    combi_arr = []
    numbers = list(numbers)    
    # 완탐으로 조합(중복X, 순서X)한 후, 매번 소수 판별 
    combi([], [False for _ in range(len(numbers))])
    
    return len(set(combi_arr))