def solution(s, skip, index):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for cur in s:
        idx = alphabet.index(cur)
        if idx == 25:
            idx = 0
        else:
            idx += 1
            
        cnt = 0
        
        while True:
            if cnt == index:
                answer += alphabet[idx-1]
                break
                
            if alphabet[idx] not in skip:
                cnt += 1
                
            if idx == 25:
                idx = 0
            else:
                idx += 1
    
    return answer