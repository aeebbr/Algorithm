# 문자 순회하다가
    # 태그는 그대로 출력
    # 여는 괄호 나오면: 태그 시작, 큐에 삽입
        # 공백 나와도 아무 일 없음  
    # 닫는 괄호 나오면: 태그 끝, 큐에서 빼기 
    
    # 큐가 비지 않았는데 문자가 나온다 => 태그 
    # 큐가 비었는데 문자가 나온다 => 단어 

    # 공백 나오면: 단어 끝 
    # 단어 시작한다면 문자열을 리스트에 저장하면서 단어 끝나는 지점 확인하기  
    # 단어 끝나면 문자열 리스트 역순으로 출력 
        # 저장한 문자열 리스트 길이만큼 순회 인덱스 건너뛰기 
        # 문자열 리스트 초기화 
from collections import deque

S = list(input())

q = deque()
word = []

for i in range(len(S)):
    cur = S[i]
    # 태그 시작 
    if cur == '<':
        q.append('<')
        print(cur, end="")
    # 태그 종료 
    elif cur == '>':
        q.pop()
        print(cur, end="")
    # 태그 내 문자 
    elif q:
        print(cur, end="")  
    # 단어 
    elif not q:
        if cur != ' ':
            word.append(cur)

        # 단어인데 공백이 나왔거나 마지막 인덱스거나 다음이 여는 괄호거나 => 단어 끝 
        if cur == ' ' or i == len(S) - 1 or S[i+1] == '<':
            # 단어 역으로 출력
            for j in range(len(word)-1, -1, -1):
                print(word[j], end="")  

            # 공백 출력     
            if cur == ' ':
                print(cur, end="")  

            # 단어 초기화 
            word = []
