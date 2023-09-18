import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for key in range(1, N+1):
    value = input().rstrip()
    dic[key] = value
    dic[value] = key

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(dic.get(int(question)))
    else:
        print(dic.get(question))