# 원소 앞뒤 바꾸기 
def solution(players, callings):
    dic = {}
    
    for i in range(len(players)):
        dic[players[i]] = i

    for cur in callings:
        cur_idx = dic[cur]
        front_idx = cur_idx - 1
        front = players[cur_idx-1]

        players[front_idx] = cur
        players[cur_idx] = front
        
        dic[cur] -= 1
        dic[front] += 1
        
    return players