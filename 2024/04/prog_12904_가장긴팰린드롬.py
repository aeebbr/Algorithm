def solution(s):
    answer = 0

    # 현재 글자를 기준으로 한 글자씩 늘려나가기 
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            # i부터 j까지 슬라이싱
            tmp = s[i:j]
            # 팰린드롬이라면
            if tmp == tmp[::-1]:
                # 최대 길이 갱신
                answer = max(answer, len(tmp))
                
    return answer