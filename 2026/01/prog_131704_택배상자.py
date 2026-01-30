from collections import deque
def solution(order):
    answer = 0
    
    origin = deque([i+1 for i in range(len(order))])
    sub = []
    
    # o번 박스 차례 
    for o in order:
        # 서브 컨베이어부터 확인 
        if sub:
            sub_box = sub[-1]
            if o == sub_box:
                sub.pop()
                answer += 1
                continue
            
        is_find = False
        # 본진 확인 
        while origin:
            origin_box = origin.popleft()
            # 본진의 박스와 불일치 -> 서브로 보내기 
            if o != origin_box:
                sub.append(origin_box)
            # 본진의 박스와 일치 -> 박스 찾음! 
            else:
                is_find = True
                answer += 1
                break
                
        # 본진에서도 못 찾음 -> 최종 실패 
        if not is_find:
            break
    
    return answer