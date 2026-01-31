'''
head, number는 필수, tail은 선택 

head는 대소문자 구분 없이 정렬 

number는 처음으로 나오는 숫자 덩어리 
number는 문자열이 아닌, 숫자 기준으로 정렬하되, 문자열로 기록해야 함 

tail은 number 뒤의 모든 문자열 
tail은 정렬에 영향을 미치지 않음 

정렬 순위: head, number, 입력순서
'''
def solution(files):
    sorted_arr = []
    
    for file in files:
        head, number = '', ''
        
        for i in range(len(file)):
            s = file[i]
            if s.isdigit():
                number += s
            else:
                if number != '':
                    break
                head += s
        
        sorted_arr.append((file, head.lower(), int(number)))
        
    sorted_arr = sorted(sorted_arr, key = lambda x:(x[1], x[2]))
    
    return [title[0] for title in sorted_arr]        