'''
dic = {
    알파벳: [개수, [알파벳 위치(인덱스번호]],
}
'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    dic = {}
    W = list(input())
    for i in range(len(W)):
        if W[i] in dic:
            dic[W[i]][0] += 1
            dic[W[i]][1].append(i)
        else:
            dic[W[i]] = [1, [i]]
    K = int(input())

    min_ans = float("inf")
    max_ans = 0

    for k, v in dic.items():
        if v[0] < K:
            continue
            
        # 범위: j 포함 K개 
        '''
        bbbababbbaabbba
        [3, 5, 9, 10, 14], K = 3이라면, 
        0, 1, 2
        1, 2, 3
        ... 
        2, 3, 4 까지. 

        => 현재 인덱스 + (K-1)번째 인덱스까지 
        '''
        for j in range(0, len(v[1])-K+1):
            start = v[1][j]
            end = v[1][j+(K-1)]

            tmp = end - start + 1
            min_ans = min(min_ans, tmp)
            max_ans = max(max_ans, tmp)

    if max_ans == 0:
        print(-1)
    else:
        print(min_ans, max_ans)