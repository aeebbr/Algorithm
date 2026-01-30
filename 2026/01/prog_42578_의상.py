from collections import Counter
def solution(clothes):
    answer = 1
    count = Counter(kind for _, kind in clothes)
    
    for v in count.values():
        # 현재 종류에서 아이템을 하나 고르는 경우 + 고르지 않는 경우 
        answer *= (v+1)
    
    # 최소 한 개는 입음 -> 전부 안 입는 경우 제외
    return answer - 1