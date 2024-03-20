S = input().rstrip()
answer = float("inf")
a_cnt = S.count('a')

'''
aba
원형: a)b(a => 평면으로 생각하면 ab(aa)b ...
'''
# 원형을 고려해서 마지막 문자에서부터 한번 더 돌게 만들기 
S += S[0:a_cnt-1]

# a 개수만큼 연속되어야 함 
# 모든 자리에서 시작하고, 각 시작점에서부터 a 개수만큼 묶어서 생각
for start in range(len(S)-a_cnt+1):
    '''
    슬라이싱한 문자열 안에 있는 b와, 슬라이싱 밖의 a를 맞바꿔서 
    a는 슬라이싱한 범위 안에만 있도록 하고, 밖에는 b만 있게하기 

    abababababbbbba
    총 길이 15, a 6개, b 9개  
    a(bababa)babbbbba

    babbbbab
    총 길이 8, a 2개, b 6개
    b(ab)bbbab
    '''
    answer = min(answer, S[start:start+a_cnt].count('b'))

print(answer)