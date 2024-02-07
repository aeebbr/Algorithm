from collections import Counter

def solution(topping):
    answer = 0
    
    dic = Counter(topping)
    set_dic = set()

    for t in topping:
        # 현재 토핑 수 빼주기 
        dic[t] -= 1 # 현재 미포함
        
        if not t in set_dic:
            # 현재 토핑 수 늘려주기 
            set_dic.add(t) # 현재 포함 
        
        # 현재 토핑의 가짓수가 0이라면 현재 토핑을 딕셔너리에서 제거 
        if dic[t] == 0:
            dic.pop(t)
        
        if len(dic) == len(set_dic):
            answer += 1
        
    return answer