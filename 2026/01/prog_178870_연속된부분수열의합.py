# 투 포인터 
def solution(sequence, k):
    answer = []
    right = 0
    total = 0
    
    for left in range(len(sequence)):
        while right < len(sequence) and total < k:
            total += sequence[right]
            right += 1
            
        if total == k:
            answer.append((left, right-1))
            
        total -= sequence[left]
    
    # 정렬 
    answer.sort(key = lambda x: [(x[1]-x[0], x[0])])
    return answer[0]