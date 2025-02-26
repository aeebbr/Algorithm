import math
def solution(A,B):
    answer = 0
    
    # 누적 값이 최소가 되려면 -> 작은값 * 큰값(큰값과 큰값을 곱하면 안됨)
    A.sort()
    B.sort(reverse=True)
    
    for ab in zip(A, B):
        answer += math.prod(ab)

    return answer