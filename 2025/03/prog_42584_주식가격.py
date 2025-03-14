'''
백준의 '레이저 탑'과 유사 
- 각 원소에서부터 마지막까지 탐색해야 함 -> 일일히 모든 원소를? 안됨 
- 맨 뒤에서부터 탐색?
    - 현재보다 작은 게 있다면, 현재는 그 작은 원소의 답임. 두 인덱스 위치를 계산해서 초를 도출하면 됨 
- 가격이 떨어진 최초의 순간을 찾아야 함 -> 최초 그 이후에는 가격이 떨어져도 쓸모 없음 

..., cur, top ... 
cur이 top보다 크든 작든 간에 cur은 항상 stack에 삽입 
cur이 top보다 크다면 top은 stack에서 유지: 가격 하락 찾음!!! 
cur이 top보다 작다면 top은 stack에서 제거: top보다 앞에 있는 cur이 더 작기 때문에, 그 앞에 더 큰 게 있다면 무조건 cur이 최초로 가격이 떨어진 순간에 해당함 
cur과 top이 같다면 top은 stack에서 제거: cur과 top을 연달아 중복으로 하는 것은 다음 탐색에서 비효율이며, 더 앞에 있는 cur의 인덱스로 갱신하는 것이 맞음 

*** cur보다 큰 top을 찾거나, stack이 바닥날 때까지 stack 내부와 비교 탐색을 해야 함!

1, 2, 3, 2, 3
3) stack: 3
2) top: 3, cur < top, stack: 2
3) top: 2, cur > top, stack: 2, 3 !!! 
2) top: 3, cur < top, stack: 2
    top: 2, cur == top, stack: 2
1: top: 2, cur < top, stack: 1

5, 7, 6, 2, 10
10> stack: 10
2> top: 10, cur < top, stack: 2
6> top: 2, cur > top, stack: 2, 6 !!! 
7> top: 6, cur > top, stack: 2, 6, 7 !!! 
5> top: 7, cur < top, stack: 2, 6
    top: 6, cur < top, stack: 2 
    top: 2, cur > top, stack: 2, 5 !!! 
'''
def solution(prices):
    # 초기화: 각 원소의 인덱스 번호를 거꾸로
    # [..., 5, 4, 3, 2, 1, 0]
    answer = [x for x in range(len(prices)-1, -1, -1)]
    stack = []
    
    for i in range(len(prices)-1, -1, -1):
        cur = prices[i]
        
        while stack: 
            top, top_i = stack.pop()

            # 가격 하락 
            if cur > top: 
                stack.append((top, top_i))
                
                # 가격이 떨어지지 않은 기간: 가격이 떨어진 위치 - 현재 위치
                answer[i] = top_i - i
                break
            
        stack.append((cur, i))
    
    return answer