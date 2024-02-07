S = int(input())

total = 0
cnt = 0

while total <= S:
    cnt += 1
    total += cnt

# while문의 마지막 턴에서 cnt + 1 했으니 되돌리기 
print(cnt - 1)
