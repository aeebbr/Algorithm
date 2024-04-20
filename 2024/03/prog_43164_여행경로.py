from collections import deque

def solution(tickets):
    answer = []
    
    tickets.sort(key = lambda x: (x[0], x[1]))
        
    q = deque()
    # (현재 탐색 중인 경로, 남은 티켓)
    q.append((["ICN"], tickets))
    
    while q:
        now_path, left_t = q.popleft()
        
        if len(left_t) == 0:
            answer = now_path
            break
            
        valid_idx = -1
        
        for i in range(len(left_t)):
            # 마지막 도착지에서 출발하는 것이라면
            if left_t[i][0] == now_path[-1]:
                valid_idx = i
                # print(i, now_path[-1], left_t)
                break
                
        # 다른 곳으로 가는 티켓이 없다면 잘못된 경로임 
        if valid_idx == -1:
            continue
            
        while valid_idx < len(left_t) and left_t[valid_idx][0] == now_path[-1]:
            q.append((now_path + [left_t[valid_idx][1]], left_t[:valid_idx] + left_t[valid_idx+1:]))
            
            # print(valid_idx, q)
            
            valid_idx += 1
        # print()   
    
    return answer

'''
# dfs
def solution(tickets):
    answer = []
    
    # 출발지가 같은 티켓끼리 쭉 나열되도록 출발지 기준 정렬
    # 같은 출발지에 대해서 도착지 기준 정렬(알파벳 순서 상 앞에꺼 먼저 방문하기 위함)
    tickets.sort(key = lambda x: (x[0], x[1]))
    
    # DFS
    def getPath(t, path):
        # 티켓을 모두 소진했다면 현재까지의 path 그대로 리턴
        if len(t) == 0:
            return path
        
        now = path[-1]
        valid_idx = -1
        
        # 남은 티켓(정렬된 상태) 중에서, 출발지가 현재 공항인 티켓의 인덱스를 찾음
        # 조건을 만족하는 티켓 중 가장 왼쪽의 티켓에서 멈춤
        for i in range(len(t)):
            if t[i][0] == now:
                valid_idx = i
                break
            
        # len(t) == 0이 아니었으므로 티켓이 남아있다는건데 나아갈 공항이 없다는 것은
        # 유효한 루트가 아니라는 뜻이므로 실패의 의미에서 빈 리스트 리턴
        if valid_idx == -1:
            return []
        
        # 출발지가 현재 공항인 티켓을 모두 순회하면서 DFS 돌림
        # 하나라도 먼저 완성된 루트가 나온다면 그걸 리턴해줌
        # 같은 출발지 기준, 도착지를 기준으로 오름차순 정렬했었기 때문에
        # 먼저 완성된 루트가 나온다면 그게 곧 알파벳 순서 상 가장 앞선 루트가 됨
        while t[valid_idx][0] == now:
            nxt_path = getPath(t[:valid_idx] + t[valid_idx + 1:], path + [t[valid_idx][1]])
            
            if nxt_path != []:
                return nxt_path
            
            valid_idx += 1
        
        return []
    
    return getPath(tickets, ["ICN"])'''