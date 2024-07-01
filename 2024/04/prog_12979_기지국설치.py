def solution(n, stations, w):
    nonS, cnt = 0, 0
    for s in stations:
        stationS = s - w - 1
        
        if stationS > nonS:
            # 전파 전달 안되는 구간 길이 
            ran = stationS - nonS
            
            value = ran // (w*2+1)
            mod = ran % (w*2+1)
            
            if mod != 0:
                cnt += value + 1
            else:
                cnt += value
            
        # 갱신 
        nonS = s + w
        
    # 마지막 기지국부터 마지막 위치까지 전파가 전달 안되는 구간의 길이 
    ran = (n-1) - (stations[-1] + w - 1)
    
    if ran > 0:
        value = ran // (w*2+1)
        mod = ran % (w*2+1)

        if mod != 0:
            cnt += value + 1
        else:
            cnt += value

    return cnt