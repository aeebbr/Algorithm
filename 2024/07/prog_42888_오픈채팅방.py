def solution(record):
    answer = []
    
    # 아이디를 기준으로 닉네임 변경 반영 
    # 아이디를 기준으로 최종적으로 엔터와 리브를 차례대로 
    
    user_dic = {}
    split_record = []
    for r in record:
        tmp = r.split()
        split_record.append(tmp)
        
        if tmp[0] != "Leave":
            user_dic[tmp[1]] = tmp[2]
        
    for r in split_record:
        if r[0] == "Enter":
            answer.append(user_dic[r[1]] + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(user_dic[r[1]] + "님이 나갔습니다.")
    
    return answer