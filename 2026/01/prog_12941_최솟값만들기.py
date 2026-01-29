# 중복으로 뽑기 불가 
# 각각의 곱이 작아야 함 
#   곱은 큰 것 * 작은 것 조합이 최적 
# A를 정렬, B를 역정렬해서 같은 자리수끼리 곱하고 누적
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
        
    for a, b in zip(A, B):
        answer += a * b

    return answer