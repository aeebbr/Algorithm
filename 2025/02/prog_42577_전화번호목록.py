def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    pre = phone_book[0]    
    for i in range(1, len(phone_book)):
        cur = phone_book[i]
        if pre == cur[:len(pre)]:
            answer = False
            break
        else:
            pre = cur
    
    return answer