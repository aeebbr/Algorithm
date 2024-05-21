import copy
from itertools import combinations, permutations

rear = []
answer = 0

def test(sel, relation):
    global rear
    global answer
    # print("***", sel)
    arr = []
    
    # 중복 확인
    for i in range(len(relation)):
        tmp = []
        for j in sel:
            tmp.append(relation[i][j])
        if tmp in arr: # 중복 -> 실패 
            return 
        
        arr.append(tmp)
            
    # 성공 
    rear.append(copy.deepcopy(sel))
    answer += 1
    # print(arr, "rear 추가", rear)
    
    return

def combi(sel, N, idx, relation):
    global rear
    if N + 1 == len(sel):
        return
    
    '''
    <틀린 사레>
    rear: [0, 1, 2]
    sel: [1, 3, 5]
    
    <옳은 사례>
    rear: [[0], [1, 2]]
    sel: [1, 3, 5]
    rear의 각 배열의 원소가 모두 sel에 들어있다면 실패 
    '''
    if len(sel) != 0:
        print(sel)
        
        if len(rear) != 0:
            # print(rear, len(rear))
            for i in range(len(rear)):
                cnt = 0
                for j in range(len(rear[i])):
                    if rear[i][j] in sel:
                        cnt += 1
                if cnt == len(rear[i]): # 최소성 불만족 
                    break 
            else: # 최소성 만족 
                test(sel, relation)
        else:
            test(sel, relation)

    for i in range(idx, N):
        sel.append(i)
        combi(sel, N, i+1, relation)
        sel.pop()

def solution(relation):
    N = len(relation[0])
    
        
    temp = [i for i in range(len(relation[0]))]
    combi_lists = list()
    # 조합 생성
    for cnt in range(1, len(relation[0]) + 1):
        combi_lists.append(list(combinations(temp, cnt)))
        
    # 조합리스트를 문자열로 변경
    combi_str_list = list()
    for combi_list in combi_lists:
        for i in combi_list:
            combi_str_list.append(''.join(map(str, i)))
        
    # print(combi_str_list)

    for sel in combi_str_list:
        sel = list(map(int, sel))
        # print(sel)
        if len(rear) != 0:
            for i in range(len(rear)):
                cnt = 0
                for j in range(len(rear[i])):
                    if rear[i][j] in sel:
                        cnt += 1
                if cnt == len(rear[i]): # 최소성 불만족 
                    break 
            else: # 최소성 만족 
                test(sel, relation)
        else:
            test(sel, relation)

        
    # combi([], N, 0, relation)
    
    return answer