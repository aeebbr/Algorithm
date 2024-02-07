N = int(input())
stack = []
answer = []
cur = 1

# N번 순회
for _ in range(N):
    # 만나야 하는 수 
    num = int(input())

    # cur이 num보다 작다면, 
    # cur이 num을 만날 때까지 오름차순으로 push
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
    
    # stack의 top이 num과 같다면
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        exit()

for ans in answer:
    print(ans)

# N = int(input())
# tmp_stack = []
# input_stack = []
# stack = [0]
# answer = []
# for i in range(N, 0, -1):
#     tmp_stack.append(i + 1)
#     input_stack.append(int(input()))

# # 만들어야 하는 순열 순회 
# for cur in input_stack:
#     # 비교할 것 
#     # 가장 최근에 pop한 값
#     pre = stack[-1]

#     if cur < pre:
#         # pop
#         # input_stack에서 pop
#         pop = input_stack.pop()
        
#         if pop != cur:
#             # 실패 
#             print("NO")
#             exit()
#         else:
#             answer.append('-')
#     else:
#         # push 
#         # cur이 나올 때까지 tmp stack에서 pop해서 stack에 push 
#         while True:
#             pop = tmp_stack.pop()
#             stack.append(pop)
#             answer.append('+')
#             if pop == cur:
#                 break
        
