from collections import deque

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

plain = deque(list(input()))
key = list(set(input()))
board = []
# 2차원 배열에 각 문자의 좌표 저장하는 딕셔너리 
alpha_position = {}

for i in alphabet:
    alpha_position[i] = (0, 0)

for a in alphabet:
    if not a in key:
        key.append(a)

# 1차원을 2차원으로 변환
for k in range(0, len(key), 5):
    board.append(key[k:k+5])

# 각 알파벳의 좌표 저장 
for i in range(5):
    for j in range(5):
        alpha_position[board[i][j]] = (i, j)

# 문자열 분해 
# 암호화한 결과  
cipher = []

# 탐색할 때마다 암호화 끝난 평문 값 줄여가기 => 평문 글자 없어질 때까지 탐색 
while plain:
    if len(plain) == 1:
        cipher.append([plain.pop(), 'X'])
        break

    a = plain.popleft()
    b = plain.popleft()

    if a != b:
        cipher.append([a, b])
    else:
        if a == 'X' and b == 'X':
            cipher.append([a, 'Q'])
        else: 
            cipher.append([a, 'X'])

        # 쌍의 두번째 값 다시 넣기 
        plain.appendleft(b)

ans = []

for pair in cipher:
    # 이번 턴의 암호 문자쌍
    a, b = pair

    # 각 암호 문자의 좌표 
    ar, ac = alpha_position[a]
    br, bc = alpha_position[b]

    # 행이 같다면
    if ar == br:
        # a 탐색
        # 마지막 열이라면 
        if ac + 1 >= 5:
            # 1번 열의 값으로 
            ans.append(board[ar][0])
        else:
            ans.append(board[ar][ac + 1])
        
        # b 탐색 
        # 마지막 열이라면 
        if bc + 1 >= 5:
            # 1번 열의 값으로 
            ans.append(board[br][0])
        else:
            ans.append(board[br][bc + 1])
    
    # 열이 같다면 
    elif ac == bc:
        # a 탐색
        # 마지막 행이라면 
        if ar + 1 >= 5:
            # 1번 행의 값으로 
            ans.append(board[0][ac])
        else:
            ans.append(board[ar + 1][ac])

        # b 탐색
        # 마지막 행이라면 
        if br + 1 >= 5:
            # 1번 행의 값으로 
            ans.append(board[0][bc])
        else:
            ans.append(board[br + 1][bc])

    # 행, 열 다 다르다면
    else:
        # 두 글자의 열 교환
        ans.append(board[ar][bc])
        ans.append(board[br][ac])

print("".join(ans))