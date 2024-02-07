brackets = input()

# 현재 막대 수 
cur_bar_cnt = 0
# 총 조각 수 
total_piece_cnt = 0

is_bracket_open = 0
    # 1. (
    # 막대 시작 -> 총 조각 + 1, 현재 막대 + 1
    # 2. )
    # 레이저 -> 총 조각 + 1
    # 막대 끝 -> 현재 막대 -1

    # 다음 괄호가 여는 괄호인지 닫는 괄호인지 따지기 
    # 따라서, 조각과 막대의 증감은 여는 괄호의 다음 괄호 탐색에서 
    # 여는 괄호 => 1
    # 닫는 괄호 => 0

for bracket in brackets:
    # 왼 괄호라면
    if bracket == '(':
        is_bracket_open = 1
        
        total_piece_cnt += 1
        cur_bar_cnt += 1
    # 오른 괄호라면 
    elif bracket == ')':
        # 이전 괄호의 종류를 확인해야 함
        # 이전 괄호가 여는 괄호라면 레이저 
        # 닫는 괄호라면 막대 끝 
        if is_bracket_open:
            # 이전 여는 괄호에서 추가한 카운트 1개를 뺌
            # 롤백
            total_piece_cnt -= 1
            cur_bar_cnt -= 1

            # 막대기 추가
            total_piece_cnt += cur_bar_cnt
            is_bracket_open = 0
        else:
            cur_bar_cnt -= 1

print(total_piece_cnt)
