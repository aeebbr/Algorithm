# q가 나오면 울음 시작 
# 순서가 핵심 

# 전체 문자열 순회하면서 하나의 울음소리 찾기
    # 방문하지 않은 문자만 탐색 
    # 카피 배열에 현재 턴 울음 방문 체크  
    # 순서대로 울음 문자 완성됐다면 카피 배열을 찐배열로 
str = input()
visited = [False] * len(str)
duck = ['q', 'u', 'a', 'c', 'k']
# 찾아야 하는 문자 
idx = 0

# 울음소리 시작 = 'q'
start_cnt = str.count('q')
cnt = 0

if len(str) % 5 != 0:
    print(-1)
    exit()

# 오리가 존재할 수 있는 최대수 
for _ in range(start_cnt):
    # 울음 시작 
    for i in range(len(str)):
        if not visited[i] and str[i] == duck[idx]:
            visited[i] = True

            # 마지막 울음소리였다면 울음 하나 완성 
            if idx == 4:
                idx = 0
            else:
                idx += 1

    # 한 턴을 마치고 나왔을 때 
    # 0으로 초기화되어 있다면 울음 하나를 완성한 것 
    if idx == 0:
        cnt += 1
    # 아니라면 울음 완성 못함 (실패)
    else:
        break

    if not False in visited:
        break 

# 최대수를 탐색했는데도 False가 남아있다면 실패 
if False in visited or cnt == 0:
    print(-1)
else:
    print(cnt)
            