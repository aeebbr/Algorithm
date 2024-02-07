# 중복 X, 조합

import sys 
sys.setrecursionlimit(10**4)

def recur(idx, sel):
    # 종료 조건
    if len(sel) == 6:
        print(*sel)
        return 

    # 1번 인덱스부터 마지막 인덱스까지 
    for i in range(idx, len(arr)):
        # 방문 처리 
        # sel에 i번째 수가 없는가  
        if not arr[i] in sel:
            # sel에 i번째 수 추가 
            sel.append(arr[i])
            recur(i + 1, sel)
            # 추가했던 i번째 수 다시 제거 
            sel.pop()

while True:
    # 0번 인덱스: k
    arr = list(map(int, input().split()))

    recur(1, [])

    if arr[0] == 0:
        break
    
    print()
