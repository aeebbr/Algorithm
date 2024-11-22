def solution(order):
    answer = 0
    stack = [] # 보조 컨테이너 
    cur_idx = 0
    
    for b in range(1, len(order)+1):
        # 보조 컨테이너 확인 
        if stack: 
            top = stack.pop()
            if top == order[cur_idx]:
                answer += 1
                cur_idx += 1                    
            else: # 뺄 게 없으면 보조 컨테이너에 넣기 
                stack.append(top)
        
        # 메인 컨테이너 확인 
        if b == order[cur_idx]: # 메인 컨테이너에서 빼내기 
            answer += 1
            cur_idx += 1   
        else:
            stack.append(b)
                
    # 보조 컨테이너 확인 
    while stack:        
        if stack.pop() == order[cur_idx]:
            answer += 1
            cur_idx += 1
        else:
            break
    
    return answer