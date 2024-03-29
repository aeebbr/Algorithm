'''
노랑의 곱 조합 
    24라면, 1/24, 2/12, 3/8, 4/6
1/24라면, 최소세로는 1+2=3 // 최소가로는 24+2=26 => 최소크기는 3*26=78, 이는 노랑+갈색=48 보다 크니까 불가 
2/12라면, 최소세로는 2+2=4 // 최소가로는 12+2=14 => 최소크기는 4*14=56, 불가 
3/8라면, 최소세로는 5, 최소가로는 10 => 최소크기는 50, 불가 
4/6라면, 최소세로는 6, 최소가로는 8 => 최소크기는 48, 이는 48에 딱 맞으니까 가능
    이 때 두 변 중 더 큰 게 세로, 작은 게 가로임 
'''
'''
1이라면, 1/1
최소세로는 3, 최소가로는 3 => 최소크기는 9, 이는 9에 맞으니까 가능 
'''

# tmp1, tmp2 = 최소 변(최소가로, 최소세로 또는 최소세로, 최소가로)
def check(tmp1, tmp2, total):
    # 최소 크기 
    min_size = tmp1 * tmp2
    # 최소크기가 총 타일의 개수보다 같거나 같아야 함
    if min_size <= total:
        return True
    return False

def solution(brown, yellow):
    for i in range(1, (yellow//2)+2):
        if yellow % i == 0:   
            tmp1, tmp2 = i+2, yellow//i+2
            if check(tmp1, tmp2, brown+yellow):
                return [max(tmp1, tmp2), min(tmp1, tmp2)]