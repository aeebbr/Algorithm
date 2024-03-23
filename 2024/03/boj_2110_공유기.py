'''
1, 2, 4, 8, 9
1 1 0 1 0 0 0 1 1 
이분탐색으로 공유기 간 최소로 보장되는 거리를 찾기 
거리를 점점 좁히거나 늘려가면서 어떤 거리일 때의 공유기 수가 N개에 들어맞는지 찾기 
'''
import sys
input = sys.stdin.readline

def binary_search(): 
    # 탐색으로 찾는 것은 거리!!! => 범위를 줄여가며 거리를 찾아야 한다!!!  
    start, end = 0, house[N-1]-house[0] # 최소 거리, 최대 거리 
    answer = 0

    while start <= end:
        mid = (start+end) // 2 # 설정된 거리 
        cur = house[0] # 현재 공유기 위치 
        target_cnt = 1 # 설치된 공유기 개수. 첫번째 공유기 개수인 1로 초기화 

        # 탐색 조건 
        # 설정된 거리 이상에 떨어진 곳에 공유기가 있는지 찾기 
        for i in range(1, N):
            if cur + mid <= house[i]:
                # 탐색 위치에 공유기 설치 
                cur = house[i]
                # 공유기 개수 증가 
                target_cnt += 1
        # 설치할 목표 개수 설정 완료 

        # 목표 개수와, C(설치해야 할 수)의 수를 비교 
        # 목표 개수가 C보다 크다면 거리를 늘이기  
            # 같은 경우도 포함 
                # 목표 거리만큼 공유기를 설치할 때, 설치할 수 있는 모든 개수이기 때문에 C개 이상이라면 그 중 C개만 택하면 되니까 답에 충족하기 때문 
        if target_cnt >= C: 
            # start를 늘이기 
            start = mid + 1
            # 현재의 거리를 답으로 갱신 
            # 결국 조건에 들어맞는 마지막 턴의 거리가 최종 답임 
            answer = mid 
        # 목표 개수가 C보다 작다면 거리를 줄이기 
        else: 
            # end를 줄이기 
            end = mid - 1

    return answer 

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

print(binary_search())
