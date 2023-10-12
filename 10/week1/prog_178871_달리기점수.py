def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i

    for c in callings:
        idx = dic[c]
        dic[c] -= 1
        dic[players[idx-1]] += 1
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
    return players