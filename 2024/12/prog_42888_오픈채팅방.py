'''
최종적으로 바뀐 아이디를 입퇴장 문구와 매치 
'''
def solution(record):
    answer = []
    name_dic = {}
    state_dic = {
        "Enter": "들어왔습니다.", 
        "Leave": "나갔습니다.", 
    }
    
    for r in record:
        tmp = r.split(" ") 
        state = tmp[0]
        
        if state != "Leave":
            i, n = tmp[1], tmp[2] # id, name        
            name_dic[i] = n
        
    for r in record:
        tmp = r.split(" ") 
        state, i = tmp[0], tmp[1]
        
        if state != "Change":
            alert = name_dic[i] + "님이 " + state_dic[state]
            answer.append(alert)

    return answer