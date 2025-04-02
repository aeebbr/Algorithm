def solution(picks, minerals):
    answer = 0
    # 각 그룹의 최악의 피로도를 담은 배열 
    groups = [] # [[그룹 피로도, 다이아 수, 철 수, 돌 수], ...]
    # 주어진 곡괭이로 캘 수 있는 광물 그룹의 수 
    total_group_cnt = sum(picks)
    
    for i in range(0, len(minerals), 5):
        # 이번 그룹(광물을 5개씩 끊음)
        group = minerals[i: i+5]
        
        # 이 그룹의 최악의 피로도: 최악의 곡괭이(돌)로 캤을 때의 피로도 
        # 각 다이아, 철, 돌의 피로도 계산하여 총합
        dia_cnt = group.count("diamond")
        iron_cnt = group.count("iron")
        stone_cnt = group.count("stone")

        cost = dia_cnt * 25 + iron_cnt * 5 + stone_cnt 
        groups.append((cost, dia_cnt, iron_cnt, stone_cnt))
    
    # 곡괭이로 캘 수 있는 광물만큼만 캐기
        # 광물은 순서대로 캐야하니 원래의 순서에서 자르기 
    groups = groups[:total_group_cnt]
        
        # 이 때, 캘 수 있는 광물은, 피로도가 높은 상위 그룹들임 
        # => 곡괭이 수만큼 상위그룹 자르기 
        # 피로도가 가장 많은 그룹부터 내림차순 정렬 
    groups.sort(key = lambda x: x[0], reverse=True)
    
    # 그룹별 피로도에 따른 곡괭이 배정 
    # 피로도가 높은 그룹부터 정렬돼 있기 때문에, 강한 곡괭이를 순서대로 배정하면 됨 
    for cost, dia_cnt, iron_cnt, stone_cnt in groups:
        # 다이아 곡괭이가 있다면 다이아 곡괭이 
        if picks[0] > 0: 
            answer += (dia_cnt + iron_cnt + stone_cnt)
            picks[0] -= 1
        # 다이아 곡괭이가 없다면 철 곡괭이 
        elif picks[1] > 0:
            answer += (dia_cnt * 5 + iron_cnt + stone_cnt)
            picks[1] -= 1
        # 철 곡괭이가 없다면 돌 곡괭이 
        elif picks[2] > 0:
            answer += (dia_cnt * 25 + iron_cnt * 5 + stone_cnt)
            picks[2] -= 1
        # 아무 곡괭이가 없다면 종료 
        else:
            break
        
    return answer