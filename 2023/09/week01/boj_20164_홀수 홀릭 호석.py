# 새로운 홀수가 나오는 위치 
# 1. 초기 입력 숫자에서 홀수 찾기 
# 2. 더하기 연산 결과에서 홀수 찾기 
# 숫자 갱신 완료될 때마다 각 값 중에 홀수 있는지 확인하여 홀수 개수 증가시키기 

'''
아래와 같은 예시에서 세 조합으로 쪼개는 경우  
A B C D E
* [:2][2:4][4:]
* [:1][1:4][4:]
* [:4][4:6][6:] ... 

=> 세 파트로 나누어 문자열 슬라이싱 
처음부터 a까지 // a부터 b까지 // b부터 끝까지  

그렇다면 a, b 인덱스 범위는 어떻게? 
1. a의 가능 범위: 1번부터 마지막 인데스 이전까지(len(텍스트) - 1)
2. b의 가능 범위: a 다음(a+1)부터 마지막 인덱스(len(텍스트))까지 
'''

def count_odd(s):
    cnt = 0
    # 숫자의 각 자리수를 탐색하며 홀수 찾기 
    for i in s:
        if int(i) % 2 != 0:
            cnt += 1
    return cnt 

# num: 이전 턴에서 새로 연산된 값, cnt: 홀수 개수 
def devided(num, cnt):
    global min_cnt, max_cnt

    # 문자열 슬라이싱을 위해 문자열로 변환 
    s = str(num)
    # 이전 턴에서 새로 추가된 홀수 개수 카운트하여 현재까지의 카운트에 누적  
        # 이 시점에서 카운트를 해야 첫 턴을 시작하면서 초기 숫자의 홀수를 찾을 수 있음 
    cnt += count_odd(s)
    
    # 현재 문자열 길이에 따라 분할해야 하는 단위가 다름 
    # 기저 조건: 한 자리라면 종료
    if len(s) == 1:
        # 홀수 개수의 최대값, 최소값 갱신 
        min_cnt = min(min_cnt, cnt)
        max_cnt = max(max_cnt, cnt)
        return 
        
    # 두 자리라면 두 개로 각각 나누기 
    elif len(s) == 2:
        # 십의 자리 + 일의 자리 
        new = num // 10 + num % 10
        devided(new, cnt)
    
    # 세 자리 이상이라면 세 개로 분할 
    else:
        # a, b 분할 
        for a in range(1, len(s)-1):
            for b in range(a+1, len(s)):
                # 문자열 슬라이싱하여 세 파트로 나누고 숫자로 더하기  
                new = int(s[:a]) + int(s[a:b]) + int(s[b:])
                devided(new, cnt)

N = int(input())

# 홀수 개수의 최대값, 최소값
min_cnt = float("inf")
max_cnt = 0

devided(N, 0)

print(min_cnt, max_cnt)
