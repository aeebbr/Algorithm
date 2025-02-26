def solution(s):
    '''
    1. 공백 기준으로 리스트로 split
    2. split한 문자열과 문자열 사이에는 공백을 넣어야 함: " ".join(리스트)
    3. 공백이 연속일 경우에는? -> 공백도 모두 살려야 함
    '''
    
    arr = s.split(" ")
    
    # 각 문자열의 첫 문자를 대문자로 변환
    for i in range(len(arr)):
        cur = arr[i]
        if len(cur) > 0:
            arr[i] = cur[0].upper() + cur[1:].lower()
        
    return " ".join(arr)