def solution(A,B):
    answer = 0

    # 작은 수 * 큰 수 
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A, B):
        answer += a * b
    
    return answer