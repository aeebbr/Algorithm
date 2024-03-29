def solution(n, lost, reserve):
    answer = n - len(lost)
    # reserve에서 빌려준 여부 
    bought = [False] * len(reserve)
    # lost에서 받은 여부 
    took = [False] * len(lost)
    
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        cur = lost[i]
        if cur in reserve:
            idx = reserve.index(cur)
            answer += 1
            bought[idx] = True
            took[i] = True

    # 순회 방향이 -> 이기 때문에, lost를 기준으로 왼쪽 번호가 우선
    for i in range(len(lost)):
        if took[i]:
            continue
        cur = lost[i]
        if cur - 1 in reserve:
            idx = reserve.index(cur-1)
            if not bought[idx]:
                answer += 1
                bought[idx] = True
                continue
        if cur + 1 in reserve:
            idx = reserve.index(cur+1)
            if not bought[idx]:
                answer += 1
                bought[idx] = True
                continue
        
    return answer