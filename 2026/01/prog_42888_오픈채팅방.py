def solution(record):
    answer = []
    user_info = {}
    log = []
    command_msg = {
        "Enter": "들어왔습니다.", 
        "Leave": "나갔습니다."
    }
    
    for r in record:
        tmp = r.split(" ")
        command, user_id = tmp[0], tmp[1]
        
        if command in ("Enter", "Change"):
            user_info[user_id] = tmp[2]
        if command != 'Change':
            log.append((command, user_id))
        
    for command, user_id in log:
        msg = user_info[user_id] + "님이 " + command_msg[command] 
        answer.append(msg)
    
    return answer