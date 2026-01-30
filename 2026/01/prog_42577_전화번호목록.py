def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        left = phone_book[i]
        right = phone_book[i+1]
        
        if left == right[:len(left)]:
            return False
    
    return True