import sys 
input = sys.stdin.readline

N = int(input())
days = [0] * 366

for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S, E+1):
        # 기간 내 모든 날짜 카운트 
        days[i] += 1

width = 0
height = 0
size = 0

# 모든 날짜 순회 
for i in range(366):
    if days[i] != 0:
        height = max(height, days[i])
        width += 1
    # 연속 일정 끝 
    else:
        size += width * height
        # 초기화 
        width = 0
        height = 0

# 마지막 날의 사이즈 
size += width * height
print(size)

# # 입력값을 시작일 기준(0번 인덱스)으로 정렬 
# # (보류)시작일이 같다면 기간이 긴 것을 먼저 배치 

# # 정렬한 리스트 순회하면서 
#     # start, end = 리스트 값
#     # (이전아이디어)현재 end와 다음 인덱스의 start가 같다면 연속된 것 => 하지만 연속된 날 뿐만 아니라 겹치는 날까지 찾아야 함 
#     # 현재 end >= 다음 인덱스 start 라면 겹치는 날이 있는 것 
#     # 이렇게 연속 or 겹치는 날을 딕셔너리에 저장 {날짜: 카운트}

#     # 연속으로 겹치기 끝났으면 현재 턴의 딕셔너리 순회하며 최대 value 찾기 => 세로 
#     # (연속 끝난 날 - 연속 시작된 날) + 1 => 가로 
#     # 세로 * 가로 = 면적 구하여 answer에 누적 

# import sys 
# input = sys.stdin.readline

# N = int(input())
# days = [list(map(int, input().split())) for _ in range(N)]
# # [start, end] => 0번 인덱스에 있는 start를 기준(key)으로 정렬 
# # start가 같을 경우 end가 큰 것을 먼저 배치 => 두 번째 기준으로 
# days = sorted(days, key=lambda x: (x[0], -x[1]))
# dic = {}
# total_size = 0

# # 겹치는 기간의 시작일, 종료일 
# start = 0
# end = 0

# for i in range(len(days)-1):
#     cur_start, cur_end = days[i]
#     next_start, next_end = days[i+1]

#     # 기간 시작일 저장
#     if start == 0:
#         start = cur_start
#         end = cur_end
#     # 날짜 겹친 경우 
#     if end >= next_start:
#         # end 갱신
#         end = max(end, next_end)

#         # 겹친 날짜: next_start ~ min(cur_end, next_end)
#         # 겹친 날짜를 딕셔너리에 저장 
#         double_start = next_start
#         double_end = min(cur_end, next_end)

#         for j in range(double_start, double_end+1):
#             # 이미 딕셔너리에 있다면 추가
#             if j in dic:
#                 dic[j] += 1
#             # 없다면 삽입 
#             else:
#                 # 날이 중복된 것이니까 2 삽입 
#                 dic[j] = 2

#         # 다음날과 겹치는 일정인데 마지막 턴이라면 면적 구하기 
#         if i == len(days)-2:
#             # 기간의 총 면적 구하기 
#             width = (next_end - start) + 1
#             # width = (cur_end - start) + 1
#             # 겹치는 날이 없어서 딕셔너리가 비어있다면(기간 하나에 대한 면적이라면)
#             if not dic:
#                 height = 1
#             else:
#                 height = max(dic.values())
#             total_size += width * height
#     # 겹치지 않는다면 
#     else:
#         # 기간의 총 면적 구하기 
#         width = (cur_end - start) + 1
#         # 겹치는 날이 없어서 딕셔너리가 비어있다면(기간 하나에 대한 면적이라면)
#         if not dic:
#             height = 1
#         else:
#             height = max(dic.values())
#         total_size += width * height
        
#         # 초기화 
#         dic = {}
#         start = 0
#         end = 0

# print(total_size)
        