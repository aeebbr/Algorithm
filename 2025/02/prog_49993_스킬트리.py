'''
skill에 없는 것은 패스 
CBD
BACDE = BCD: 102
CBADF = CBD: 012
AECB = CB: 01
BDA = BD: 12
'''
def solution(skill, skill_trees):
    answer = 0
    dic = {}
    for i in range(len(skill)):
        dic[skill[i]] = i
    
    for s in skill_trees:
        now_learn = 0
        for ss in s:
            if ss not in dic:
                continue 

            skill_num = dic[ss]
            if now_learn == skill_num: 
                now_learn += 1
            else:
                break
        else:
            answer += 1
    
    return answer