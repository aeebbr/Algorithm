'''
스택 사용 
top이랑 나랑 둘만 비교해나가면 됨 
top이 나보다 작으면 top 제거, 나 삽입 
'''
def solution(number, k):
    number = list(map(int, number))
    stack = [number[0]]
    
    for i in range(1, len(number)):
        num = number[i]
        
        while stack:
            if k == 0:
                break

            top = stack[-1]
            
            if top < num:
                stack.pop()
                k -= 1
            else:
                break
                
        stack.append(num)
    
    # 제거해야 하는 개수 남아있으면 뒤를 자르기 
    if k > 0:
        stack = stack[:len(stack)-k]
    
    return ''.join(map(str, stack))