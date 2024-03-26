'''
[6, 5, 3, 2, 1, 0]
0번: 6, 1개 (h=1)
1번: 5, 2개 (h=2)
2번: 3, 3개 (h=3)
3번: 2, 4개 (h=2)
4번: 1, 5개 (h=1)

=> min(값, index+1) 
'''

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for i in range(len(citations)):
        answer = max(answer, min(citations[i], i+1))
            
    return answer