def solution(sequence):
    answer = 0    
    pulse = 1
        
    # 누적합 
    sel_1 = [sequence[0] * pulse] # 1부터 시작
    sel_2 = [sequence[0] * -pulse] # -1부터 시작
    for i in range(1, len(sequence)):
        pulse *= -1            

        sel_1.append(max(0, sel_1[-1]) + (sequence[i] * pulse))
        sel_2.append(max(0, sel_2[-1]) + (sequence[i] * -pulse))

    answer = max(max(sel_1), max(sel_2))
    
    return answer