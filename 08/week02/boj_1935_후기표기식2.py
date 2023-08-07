import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().rstrip('\n'))
dic = {}
# 연산되는 수 저장 
stack = []

for s in arr:
    if s.isalpha():
        # 알파벳과 숫자 딕셔너리에 매칭
        if s not in dic:
            dic[s] = int(input())
        stack.append(dic[s])
    else:
        right = stack.pop()
        left = stack.pop()

        if s == '+':
            stack.append(left + right)
        elif s == '-':
            stack.append(left - right)
        elif s == '*':
            stack.append(left * right)
        elif s == '/':
            stack.append(left / right)

print(f"{stack.pop():.2f}")

