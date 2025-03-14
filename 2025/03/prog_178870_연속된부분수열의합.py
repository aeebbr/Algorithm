# 투 포인터 
def solution(sequence, k):
    answer = []
    total = 0
    right = 0
    
    for left in range(len(sequence)):
        # right 포인터 늘려가며 탐색 
        while right < len(sequence) and total < k:
            total += sequence[right]
            right += 1
            
        # answer 갱신 
        if total == k:
            # 이미 이전에 찾은 것이 있다면 갱신 가능 여부 확인 
            if not answer:
                answer = [left, right-1]
            else:
                # 길이가 더 짧은 것으로 갱신, 길이가 같다면 갱신하지 않음 
                if (right-1) - left < answer[1] - answer[0]:
                    answer = [left, right-1]
    
        # left에서부터 right까지 탐색했으니 다음 턴에서는 현재의 left만 빼고 탐색 
        total -= sequence[left]
        
    return answer