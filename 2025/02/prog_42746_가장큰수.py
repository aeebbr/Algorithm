'''    
input: [3, 30, 34, 5, 9]

30 vs 3의 경우, 330이 아닌 303으로 정렬되는 이슈 

=> 
tmp = list(map(str, [999, 555, 343434, 333, 303030]))
tmp.sort(reverse=True)
print(tmp) # ['999', '555', '343434', '333', '303030'] 
'''
def solution(numbers):
    # 3, 30, 34, 5, 9 => 999, 555, 343434, 333, 303030 => 9, 5, 34, 3, 30
    numbers = sorted(list(map(str, numbers)), key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers))) # 예외: [0, 0, 0] 인 경우 "0" 처리 위해 str -> int -> str 형 변환  