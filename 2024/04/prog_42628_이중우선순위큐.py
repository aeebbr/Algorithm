import heapq

def solution(operations):
    q = []
    
    for o in operations:
        a, b = o.split()
        if a == 'I':
            heapq.heappush(q, int(b))
            heapq.heapify(q)
            
        else:
            if not q:
                continue
            if b == '1':
                q = heapq.nlargest(len(q), q)[1:]
                heapq.heapify(q)
                
            elif b == '-1':
                heapq.heappop(q)
        
    if q:
        return [heapq.nlargest(1, q)[0], heapq.nsmallest(1, q)[0]]
    else:
        return [0,0]
    