'''
{
C: 0, 
B: 1, 
D: 2
}
BACDE -> BCD -> 102
CBADF -> CBD -> 012
AECB -> CB -> 01
BDA -> BD -> 12

1. 딕셔너리 만들기 
2. 스킬트리를 숫자로 치환 
3. 각 스킬트리 적부 따지기 
'''

def solution(skill, skill_trees):
    answer = 0
    dic = {}
    
    for i in range(len(skill)):
        dic[skill[i]] = i
        
    for i in range(len(skill_trees)):
        skill = skill_trees[i] # 스킬 하나 
        cnt = 0
        for j in range(len(skill)): 
            s = skill[j]
            if s not in dic:
                continue
                
            number = dic[s]
            if number != cnt: # 실패 
                break
                
            cnt += 1
        else:
            answer += 1
        # 스킬 하나 탐색 끝 
        
    return answer