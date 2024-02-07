import sys 
sys.setrecursionlimit(10**4)

# idx: 현재 몇 번째 문자를 보고 있는가 
def recur(idx, sel):
    # 종료 조건
    if len(sel) == L:
        # 모음, 자음 개수 체크 
        moeum = 0
        saeum = 0
        for s in sel:
            if s in ['a', 'e', 'i', 'o', 'u']:
                moeum += 1
            else:
                saeum += 1

        if moeum >= 1 and saeum >= 2:
            print("".join(sel))
        return 

    for i in range(idx, C):
        # 해당 문자가 sel에 아직 없는가?  
        if not arr[i] in sel:
            sel.append(arr[i])
            recur(i + 1, sel)
            sel.pop()

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

recur(0, [])