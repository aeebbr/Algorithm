def solution(s):
    arr = sorted(map(int, s.split(" ")))
    return " ".join(map(str, [arr[0], arr[-1]]))