def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        answer = max(answer, min(i+1, citations[i]))
    
    return answer