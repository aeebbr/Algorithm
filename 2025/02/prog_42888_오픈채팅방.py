def solution(record):
    answer = []
    user_dic = {} # {user_id: nickname, ...}
    state_dic = {
        'Enter': '들어왔습니다.', 
        'Leave': '나갔습니다.'
    }

    for r in record:
        tmp = r.split()
        
        if len(tmp) == 2:
            continue
            
        user_id, nickname = tmp[1], tmp[2]
        user_dic[user_id] = nickname
        
    for r in record:
        tmp = r.split()
        state = tmp[0]
        user_id = tmp[1]
        
        if state != "Change":
            text = user_dic[user_id] + "님이 " + state_dic[state]
            answer.append(text)
    
    return answer