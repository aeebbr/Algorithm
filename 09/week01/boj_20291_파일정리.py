import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    file, type = input().rstrip().split('.')
    
    if type in dic:
        dic[type] += 1
    else:
        dic[type] = 1

dic = dict(sorted(dic.items()))

for k, v in dic.items():
    print(k, v)