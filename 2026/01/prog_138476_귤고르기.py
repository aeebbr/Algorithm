# 각 종류별 개수 카운트 
# 개수가 많은 종류부터 누적하다가, k에 도달하면 누적 끝. 그 때의 종류 개수 return 
from collections import Counter

def solution(k, tangerine):
    answer = 0
#   tangerine의 종류를 개수별로 카운트한 것을, 개수 기준으로 오름차순 정렬
    dic = sorted(Counter(tangerine).items(), key = lambda x: x[1])
    limit = len(dic)
    
    for _ in range(limit):
        if k <= 0:
            break
            
        k -= dic[-1][1] # 현재 종류의 개수만큼 빼기 
        answer += 1 # 현재 종류 선택 
        dic.pop()
    
    return answer