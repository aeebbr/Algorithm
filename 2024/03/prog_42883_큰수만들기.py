def solution(number, k):
    answer = [] # stack 
    rest_k = k # 남은 제거 가능 개수
    for n in number:
        n = int(n)
        
        while len(answer) > 0 and rest_k > 0 and answer[-1] < n:
            # n이 스택 안의 값보다 크다면 스택 값 제거 
            answer.pop()
            rest_k -=1
            
        # n이 현재 턴의 최대값임 
        answer.append(n)
    
    # 제거해야 할 개수가 남아있다면 
    if rest_k != 0:
        answer = answer[:-rest_k]
    
    return ''.join(map(str, answer))
    