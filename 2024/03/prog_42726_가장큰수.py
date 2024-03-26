def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))    
    numbers.sort(key = lambda x: x*3, reverse=True)
    for n in numbers:
        answer += n
        
    return str(int(answer))