def solution(citations):
    for i in range(max(citations), -1, -1):
        a=[1 for j in citations if j>=i]
        if len(a) >=i :
            return i