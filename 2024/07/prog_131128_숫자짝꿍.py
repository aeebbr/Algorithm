def solution(X, Y):
    # 겹치는 수가 없는 경우의 출력값으로 초기화 
    answer = '-1'
    
    # 가장 큰 수: 내림차순 정렬해서 만들기 
    # 겹치는 수 없으면 -> -1 리턴
    # 겹치는 수가 0만 있으면 -> 0 리턴 
        
    # 각 문자열에서 각 수의 개수 카운팅 
    dic = {}
    for x in X:
        if x in dic:
            dic[x][0] += 1
        else:
            dic[x] = [1, 0]
    for y in Y:
        # y가 딕셔너리에 이미 있는 경우에만 카운팅
            # 없다면 X와 겹치는 게 아니기 때문 
        if y in dic:
            dic[y][1] += 1
    
    # 겹치는 수 찾기 
    nums = []
    for k, v in dic.items():
        # 겹치는 수의 개수 
        cnt = min(v)
        # 1개 이상 겹친다면 
        if cnt != 0:
            # 수의 개수만큼 추가 
            for _ in range(cnt):
                nums.append(k)
                
    # 가장 큰 수 만들기 
    nums.sort(reverse=True)
    
    # 첫번째 수가 0이라면 전부 0인 것
    if len(nums) != 0:
        if nums[0] == '0':
            answer = '0'    
        else:
            answer = ''.join(nums)
        
    return answer