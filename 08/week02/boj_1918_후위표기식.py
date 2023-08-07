# 식을 순회하다가 연산자를 만난다면, 그 연산자 이전에 이미 계산되었어야 하는 연산자를 답에 이어 붙이기 
# 이미 계산되었어야 하는 연산자는: 현재 연산자 우선 순위 이상의 연산자 
# 연산자들은 stack에 넣고 있다가, 이어 붙어야 할 때 pop하기 

arr = list(input())
answer = ''
stack = []

# 식 순회 
for cur in arr:
    # 연산자가 아니라면
    if cur.isalpha():
        answer += cur
    # 연산자라면
    else:
        # 연산자별로 처리 
        if cur == '(':
            stack.append(cur)
        elif cur == '*' or cur == '/':
            # stack에 있는 *나 /를 빼서 답에 이어 붙이기 
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            # 현재 연산자를 stack에 넣기 
            stack.append(cur)
        elif cur == '+' or cur == '-':
            # ( 빼고 전부 넣기
            # ( 가 stack에 있다는 것은, 는 + 혹은 - 연산자가 괄호 안에 감싸져서 우선 연산해야 한다는 것이고, 
            # 괄호 바깥의 연산자는 아직 연산되어서는 안된다는 것
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(cur)
        elif cur == ')':
            # 괄호 한 쌍 완성
            # 해당 괄호 쌍 내의 연산자들을 전부 연산 처리 
            while stack and stack[-1] != '(':
                answer += stack.pop()
            # 괄호 내의 모든 연산 완료 했으니, 괄호 더 이상 없어도 됨 
            # 왼 괄호 제거 
            stack.pop() 

# stack에 남은 연산자 처리 
while stack:
    answer += stack.pop()

print(answer)