'''
한 글자만 다른 단어로 이동
-> 또 한 글자만 다른 단어로 이동 (이 때, 이미 방문한 단어는 이동하지 않음)
-> 반복
-> 타겟에 도달하면 종료 

hit -> hot, dot, lot
hot -> dot, dog
dot -> dog, lot
lot -> log
dog -> log, cog
=> 빨리 도달하는 게 정답, bfs
'''

from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    
    while q:
        cur, cnt = q.popleft()
        
        if cur == target:
            return cnt
        
        for i in range(len(words)):
            next = words[i]
            if visited[i]:
                continue
                
            # 한 글자만 다른지 판별
            same_cnt = 0
            for j in range(len(cur)):
                if same_cnt > (len(cur)-1):
                    break
                if cur[j] == next[j]:
                    same_cnt += 1
            if same_cnt == (len(cur)-1):
                q.append((next, cnt + 1))
                visited[i] = True

def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)
    