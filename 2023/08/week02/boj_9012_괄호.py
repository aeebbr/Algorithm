T = int(input())

for _ in range(T):
    stack = []
    brackets = list(input())

    for b in brackets:
        if b == '(':
            # stack에 추가 
            stack.append(b)
        else:
            # stack이 비어 있다면 쌍 실패 
            # stack에서 뺀 괄호가 왼 괄호가 아니라면, 쌍 실패  
            if not stack or stack.pop() != '(':
                print("NO")

                # 현재 테케 종료 
                break
    else:
        # 오른 괄호의 쌍을 다 찾아줬는데도 stack에 남은 왼 괄호가 있다면 실패 
        if stack:
            print("NO") 
        # 쌍 실패가 하나도 나오지 않았다면 성공 
        else:
            print('YES')
            

