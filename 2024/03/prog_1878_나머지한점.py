'''
짝이 안 맞는 좌표 찾기 

dic = {
    숫자: [엑스개수, 와이개수]
}
'''
def solution(v):
    answer = [0, 0]
    dic = {}
    
    for dot in v:
        for i in range(2):
            cur = dot[i]
            if cur not in dic:
                dic[cur] = [0, 0]
            dic[cur][i] += 1
    # print(dic)
    
    for k, v in dic.items():
        for i in range(2):
            if v[i] == 1:
                answer[i] = k
    return answer