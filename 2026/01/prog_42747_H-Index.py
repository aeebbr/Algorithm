# h는 최대 n
# h부터 하나씩 줄여가면서 탐색 
# 0, 1, 3, 5, 6
# -> 방향으로 탐색, 원소가 n-i보다 크거나 같은 최초의 순간 찾기 
def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= (n-i):
            answer = n-i
            break
    
    return answer