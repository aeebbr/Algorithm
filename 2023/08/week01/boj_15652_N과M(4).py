import sys 
sys.setrecursionlimit(10 ** 4)

# 중복 조합
def combi(num, sel):
    if len(sel) == M:
        print(*sel)
        return 
    
    for i in range(num, N + 1):
        sel.append(i)
        combi(i, sel)
        sel.pop()

N, M = map(int, input().split())

combi(1, [])