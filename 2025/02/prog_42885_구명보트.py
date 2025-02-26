from collections import deque
def solution(people, limit):
    '''
    1. 가장 무거운 사람은 무조건 탑승 
    2. 가장 가벼운 사람 탑승 시도, 초과하면 무효 
    '''
    answer = 0
    people.sort()
    q = deque(people)

    while q:
        answer += 1
        heavy = q.pop()
        
        if q:
            light = q.popleft()
            # 가벼운 사람 탑승 무효 
            if light + heavy > limit:
                q.appendleft(light)
    
    return answer