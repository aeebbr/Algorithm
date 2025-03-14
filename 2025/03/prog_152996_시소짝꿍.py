# 시소짝꿍: 왼쪽 사람 무게 * 왼쪽 거리 = 오른쪽 사람 무게 * 오른쪽 거리 
from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)

    # 무게가 같은 사람 구하기 
    for k, v in counter.items():
        if v >= 2:
            answer += sum(list(range(v)))
    
    # 중복제거 
    weights = list(set(weights))
    
    # 2:3, 2:4, 3:4 비율인 쌍 개수 구하기 
    for w in weights:
        # 100, 200: 100*4 = 200*2
            # => 2:4
            # 100 = 200*2/4
        # 180, 270: 180*3 = 270*2
            # => 3:2
            # 180 = 270*2/3
        if w*2/3 in counter:
            answer += counter[w] * counter[w*2/3]
        if w*2/4 in counter:
            answer += counter[w] * counter[w*2/4]
        if w*3/4 in counter:
            answer += counter[w] * counter[w*3/4]
            
    return answer