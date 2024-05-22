import copy

N = int(input())
if N == 1:
    print("*")
    exit(0)

M = 4*(N-1)+1

answer_1 = []
answer_2 = []

def recur_1(arr, idx_1, idx_2, cnt, N):
    answer_1.append(copy.deepcopy(arr))

    if cnt == N-1:
        return 
    
    arr[idx_1] = " "
    arr[idx_2] = " "

    recur_1(arr, idx_1 + 2, idx_2 - 2, cnt+1, N)

def recur_2(arr, idx_1, idx_2, cnt, N):
    answer_2.append(copy.deepcopy(arr))

    if cnt == N-2:
        return 
    
    arr[idx_1] = "*"
    arr[idx_2] = "*"

    recur_2(arr, idx_1 + 2, idx_2 - 2, cnt+1, N)

tmp = ["*"] * M
recur_1(tmp, 1, M-2, 0, N)
tmp = [" "] * M
tmp[0], tmp[M-1] = "*", "*"
recur_2(tmp, 2, M-3, 0, N)

for i in range(N):
    print("".join(answer_1[i]))
    if i == N-1:
        break
    print("".join(answer_2[i]))


for i in range(N-2, -1, -1):
    print("".join(answer_2[i]))
    print("".join(answer_1[i]))

