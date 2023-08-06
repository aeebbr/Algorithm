from collections import deque
import copy
import sys
sys.setrecursionlimit(10**4)

q = deque()
# 괄호 쌍의 인덱스 
pair = []
answer = []

# pair에서 조합
def combi(idx, sel):
    if len(sel) > len(pair):
        return 
    
    # 조합할 때마다 answer에 삽입
    if len(sel) > 0:
        # print(sel)

        bracket_removed = copy.deepcopy(bracket)
        # 괄호 제거 
        for l, r in sel:
            # 제거할 괄호가 있는 곳을 공백 처리 
            bracket_removed[l] = ''
            bracket_removed[r] = ''

        answer.append("".join(bracket_removed))

    for i in range(idx, len(pair)):
        sel.append(pair[i])
        combi(i + 1, sel)
        sel.pop()

bracket = list(input())

for i in range(len(bracket)):
    if bracket[i] == '(':
        q.append(i)
    elif bracket[i] == ')':
        left = q.pop()

        pair.append([left, i])
        
# 괄호 쌍을 조합 
combi(0, [])

# 중복 제거 
# ((2)) 의 반례에서는 (2), (2), 2가 출력됨
# 서로 다른 식을 출력하라고 했으니 중복 값은 제거해야 함
answer = set(answer)
answer = sorted(answer)

for ans in answer:
    print(ans)
