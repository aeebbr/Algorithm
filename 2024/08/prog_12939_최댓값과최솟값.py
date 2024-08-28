def solution(s):
    tmp = sorted(map(int, s.split()))
    return " ".join(map(str, [tmp[0], tmp[-1]]))