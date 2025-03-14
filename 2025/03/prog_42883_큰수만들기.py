'''
<조건> 
숫자 순서 유지하면서 제거해야 함

앞에서부터 작은 숫자 k개 제거해야 함
    앞에서부터 하는 이유: 큰 수가 되려면 큰 수는 최대한 앞에 있어야 하고, 그러므로 작은 수는 앞에서부터 제거되어야 하기 때문 

stack 안에 들어가야 하는 수: 큰 수 => stack보다 n이 더 크다면 n으로 교체 
1924
stack: [], n: 1, stack: [1]
stack: [1], n: 9, -1: 1, stack: [9]
stack: [9], n: 2, -1: 9, stack: [9]
stack: [9, 4]
'''
def solution(number, k):
    stack = [] 
    
    # 앞에서부터 탐색하며 작은 수 제거 
    for n in number:
        n = int(n)
        
        # stack 탐색하면서, stack 안의 n보다 작은 수는 모두 제거 
        # 조건: stack이 비어있지 않아야, 제거해야 하는 개수가 남아있어야 
        while len(stack) > 0 and k > 0:
            top = stack[-1]
            # n이 top보다 크다면, top을 stack에서 제거 
            if n > top:
                stack.pop()
                k -= 1
            # top이 n보다 크거나 같다면, 더 이상 stack 탐색하지 않음
            else:
                break
            
        # n은 무조건 삽입
        stack.append(n)
    
    # 만약 제거해야 하는 개수가 남아있다면 뒤를 자르기
        # 뒤를 자르는 이유: 앞은 이미 큰 수를 남겨뒀기 때문 
    # 중복되는 수가 있을 경우 이런 상황 발생함 
        # "7777777", 2 => stack: [7, 7, 7, 7, 7, 7, 7]
    if k > 0:
        stack = stack[:(len(stack)-k)]
    
    return ''.join(list(map(str, stack)))