def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        tmp = []
        for s in skills:
            if s in skill:
                tmp.append(s)
                
        # 판별 
        for i in range(len(tmp)):
            if tmp[i] != skill[i]:
                break
        else:
            answer += 1
            
    return answer