'''
순서대로 스킬에 번호 부여 
c: 0, b: 1, d: 2
스킬 간 1씩 차이 => 각 스킬을 배울 때마다 1씩 누적 
c를 배우면 1이 되고, 
b를 배우면 2가 되는. 

만약 b가 나왔는데 1이 아니라면, c를 배우기 전이라는 의미 => b를 배울 수 없는 상태임 
'''
def solution(skill, skill_trees):
    answer = 0
    
    dic = {}
    for i in range(len(skill)): 
        dic[skill[i]] = i
        
    for st in skill_trees:
        learn_total = 0
        
        for s in st:
            # 사전에 없는 스킬이면 무시 
            if s not in dic:
                continue
            
            num = dic[s]
            
            # 스킬 배울 수 있는 상태
            if learn_total == num:
                learn_total += 1
            # 스킬 배울 수 없는 상태 
            else:
                break
        # 스킬 정상적으로 배움 
        else:
            answer += 1
    
    return answer