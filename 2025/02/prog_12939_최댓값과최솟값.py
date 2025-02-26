def solution(s):    
    # 문자열 -> 숫자 리스트 변환 
    number_arr = sorted(list(map(int, s.split())))
    return " ".join(list(map(str, [number_arr[0], number_arr[-1]])))