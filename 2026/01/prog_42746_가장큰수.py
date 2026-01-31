# 34, 30, 3 -> 3434, 3030, 33
# 547, 54, 5 -> 547547, 5454, 55 => 5, 547, 54
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*4, reverse=True)
    
    return str(int("".join(numbers)))