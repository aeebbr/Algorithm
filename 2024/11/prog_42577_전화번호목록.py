def solution(phone_book):
    answer = True
    phone_book.sort()
    
    # 앞뒤만 비교 
    for i in range(len(phone_book)-1):
        pre = phone_book[i]
        cur = phone_book[i+1]
        
        length = len(pre)
        if pre == cur[:length]:
            answer = False
            break
    
    return answer