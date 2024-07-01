def solution(participant, completion):
    # 각 정렬 
    participant.sort()
    completion.sort()
    
    answer = participant[len(participant)-1]
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    return answer