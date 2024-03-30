# 내야할 총 이용료 - 처음 가지고 있던 금액
# (3) + (3+3) + (3+3+3) + (3+3+3+3) = 30 (10 * 3)
def solution(price, money, count):
    answer = -1
    total_price = sum(range(1, count+1)) * price
    
    if total_price < money:
        answer = 0
    else:
        answer = total_price - money
    
    return answer