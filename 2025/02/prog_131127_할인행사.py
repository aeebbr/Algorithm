'''
현재부터 10일간의 할인 품목의 개수를 카운트하기: dictionary
날이 바뀔 때마다 매번 세지 말고, 날이 빠지고 추가된 때의 품목의 개수만 갱신하기: 품목 일치하면 number에서 -1씩 하기 
모든 품목 가능하면(number 모두 0이면) 성공, 종료 
    모두 number인지 확인은 매번 하기: 어차피 number의 길이가 최대 10임 => 가능할 듯 
'''
from collections import deque
def solution(want, number, discount):
    def is_all_buy(arr):
        for a in arr:
            if a > 0:
                return False
        return True
    
    answer = 0
    q = deque(discount[10:])
    dic = {}
    
    # 원하는 품목의 인덱스 번호 
    for i in range(len(want)):
        dic[want[i]] = i
    
    # 초기화: 첫 10일의 각 품목 개수 확인 
    for i in range(10):
        cur = discount[i]
        if cur in dic:
            idx = dic[cur]
            number[idx] -= 1
            
    if is_all_buy(number):
        answer += 1
            
    remove_idx = 0
    # 11일차의 품목부터 확인 
    while q:
        # 전날의 품목 제거 
        pre = discount[remove_idx]
        if pre in dic:
            pre_i = dic[pre]
            number[pre_i] += 1
        
        # 추가된 날의 품목 추가 
        cur = q.popleft()
        
        if cur in dic:
            cur_i = dic[cur]
            number[cur_i] -= 1
        
        # 전품목 구매 가능 여부 확인 
        if is_all_buy(number):
            answer += 1
        remove_idx += 1
    
    return answer