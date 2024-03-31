# 일의 자리에 매칭
first_match = [4, 1, 2]

total = []
def recur(cur):
    global total
    
    value = cur // 3 # 몫
    other = cur % 3 # 나머지 
    
    # 일의 자리 추가 
    total.append(first_match[other])
    
    if value == 0 or ((value-1) == 0 and other == 0):
        return 
    
    if other == 0:
        recur(value-1)
    else:
        recur(value)

def solution(n):
    global total
    answer = ""
    recur(n)
    
    while total:
        answer += str(total.pop())
    
    return answer