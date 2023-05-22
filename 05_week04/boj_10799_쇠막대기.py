brackets = input()

# 현재 막대 수 
cur_bar_cnt = 0
# 총 조각 수 
total_piece_cnt = 0

stack = 0

for bracket in brackets:
    # 왼 괄호라면
    if(bracket == '('):
        stack += 1
    # 오른 괄호라면 
    elif(bracket == ')'):
        stack -= 1
        
