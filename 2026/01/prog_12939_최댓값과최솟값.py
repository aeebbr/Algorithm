def solution(s):
    nums = list(map(int, s.split()))
    return " ".join(map(str, (min(nums), max(nums))))