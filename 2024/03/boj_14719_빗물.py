import sys
input = sys.stdin.readline

answer = 0
H, W = map(int, input().split())
board = [[0] * W for _ in range(H)]
block = list(map(int, input().split()))
block_idx = [[-1] for _ in range(H)] # 각 행 별 블록 인덱스 번호 
for i in range(W):
    height = block[i]

    # 현재 열의 밑 행에서부터 블록 세우기  
    for j in range(H-1, H-height-1, -1):
        board[j][i] = 1
        # 블록 위치 저장하기 
        block_idx[j].append(i)

# board 윗 행부터 확인
for i in range(H):
    '''
    현재 행의 블록 위치로 물 칸 개수 확인 
    [0, 3, 4] 라면, 
    0 ~ 3 구간: 2개 (3-0-1)
    3 ~ 4 구간: -1 => 0개
    '''
    cur_block_idx = block_idx[i]
    for j in range(0, len(cur_block_idx)-1):
        if cur_block_idx[j] == -1:
            continue
        cur = cur_block_idx[j]
        next = cur_block_idx[j+1]
        water = next - cur - 1
        if water > 0:
            answer += water

print(answer)
