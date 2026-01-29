# 짝을 지을 때, 남는 무게가 최대한 없도록 꽉 채워서 짓기 
#   -> 그렇다면 최소와 최대를 짝 짓기 
#   -> 최소와 최대의 합이 limit보다 크다면, 어차피 해당 최대는 짝을 지을 수 없음. 최대인 한 명만 보트에 보내고, 제외시키기 반복 
#       이 때, 리스트에서 매번 제거 시키면 오버 스펙(?) => 투 포인터 쓰는 게 효율적 
def solution(people, limit):
    answer = 0
    people.sort()
    
#   투 포인터 
    min_person = 0 # left pointer
    max_person = len(people) - 1 # right pointer
    
    while min_person <= max_person:        
        if (people[min_person] + people[max_person]) > limit:
#           max_person 혼자만 태워 보내고 제외 
            max_person -= 1
            answer += 1
        else:
#           min_person, max_person 둘 다 태워 보내고 제거 
            min_person += 1
            max_person -= 1
            answer += 1
            
    return answer