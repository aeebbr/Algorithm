# 세번째 try(성공)
def solution(orders, course):
    answer = []
    idx_dic = {} # course의 인덱스 번호를 담은 배열 
    dic = {} # 단품메뉴 조합을 담은 딕셔너리, {단품메뉴: 메뉴 주문 회수}
    
    # course의 인덱스 번호 저장하기  
    for i in range(len(course)):
        idx_dic[course[i]] = i
    
    # 각 orders의 모든 조합 내기 
    def combi(idx, sel, order, dic):
        # 해당 조합의 단품 개수가 course 안에 있다면 dic에 저장 
        if len(sel) in course: 
            tmp = ("").join(sel) # 문자열로 변환해서 저장     
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
                
        if idx == len(order):
            return 
        
        for i in range(idx, len(order)):
            sel.append(order[i])
            combi(i+1, sel, order, dic)
            sel.pop()
            
    for order in orders:
        order = list(order)
        order.sort()
        combi(0, [], order, dic)
    
    # 단품 개수별 최대 주문 회수 저장 
    max_cnt = [0] * (len(course))
    # 단품 개수별 조합 메뉴 저장
    result = [[] for _ in range(len(course))]
    
    # 모든 조합 탐색 
    for k, v in dic.items():
        i = idx_dic[len(k)] # 현재 조합 정보를 저장할 위치. 인덱스 번호 
        
        # 주문 회수가 2회 이상이어야 함 
        if v >= 2:
            # 해당 단품 개수 중에서 최대 주문 회수인지 확인 
            if max_cnt[i] < v:
                result[i] = [k]
                max_cnt[i] = v
            elif max_cnt[i] == v:
                result[i].append(k)
                
    # print(result)
    
    for r in result:
        answer.extend(r)
        
    answer.sort()
    
    return answer

""" 두번째 try(실패)

# 유의: '가장 많이 함께 주문한' -> 같은 갯수의 조합이라면, 주문 횟수가 가장 많은 것을 채택해야 함 

# 아아아... 아래 알고리즘도 실패. 2개씩만 조합됨 

'''
"ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"

개수가 적은 주문부터 탐색 (안해도 무방한가?)
-> 작은 집합에서부터 큰 집합으로 경우의 수를 따지기 
-> ex. AB나 CD의 조합이 다른 집합에도 있는지 확인 

dic = {
    2: [(1, ab)]
    ... 
}

1. ab 탐색 
    ab의 개수가 course 안에 있는지 확인 
    있다면, ab가 다른 집합에도 있는지 확인 
    그 개수를 카운트 
        abcde 안에 있음 => 1회 
    
    (주문 횟수, 단품명 오름차순으로) 를 현재 개수 2의 딕셔너리 값에 저장된 조합과 비교, 
        이것의 횟수가 더 높다면 교체
        횟수가 같다면 추가 
    (1, ab) 저장 
2. cd 탐색 
    cd의 개수가 course 안에 있음 
    cd가 abcde, acd 안에 있음 => 2회 
    기존에 저장되어 있던 (1, ab)의 1회보다 크기 때문에 교체
    (2, cd) 저장 
3. acd 탐색 
... 반복 
'''

'''
1번 ~ 3번 손님 
x: 1, 2, 3
y: 1, 2
z: 1
w: 2, 3
a: 3

x: 1, 2, 3
y: 1, 2
w: 2, 3

이건 set 함수 쓰기 
x, w => 2, 3번에게 공통으로 
x, y => 1, 2번에게 공통으로 

'''

def solution(orders, course):
    answer = []
    
    # 일단은 작은 집합에서 큰 집합으로 탐색 
    # orders = sorted(orders, key = lambda x: len(x)) # 단품 개수를 기준으로 오름차순 정렬 
    # print(orders)
    
    # dic = {}
    
    menu = {}
    menu_idx = {}
    customer = []
    idx = 0
    for i in range(len(orders)):
        order = list(orders[i])

        for o in order:
            # if o in dic:
            if o in menu:
                # dic[o].add(i+1)
                customer[menu[o]].add(i+1)
            else:
                # dic[o] = {i+1}
                # 메뉴명: 인덱스 번호 
                menu[o] = idx
                menu_idx[idx] = o
                customer.append({i+1})
                idx += 1
    print(menu)
    print(menu_idx)
    print(customer)
    print()
    for i in range(len(customer)):
        cur = customer[i]
        
        if len(cur) == 1:
            continue
            
        for j in range(i+1, len(customer)):
            near = customer[j]
            
            if len(near) == 1:
                continue
                
            inter = cur.intersection(near)
            if inter and len(inter) > 1:
                print(menu_idx[i], menu_idx[j], ": ", cur, near, inter)

    return answer
"""

""" 첫번째 try(실패)

# 유의: '가장 많이 함께 주문한' -> 같은 갯수의 조합이라면, 주문 횟수가 가장 많은 것을 채택해야 함 

# 아아아... 아래 알고리즘 실패. 조합이 orders에 원형으로 없을 수도 있음. 마지막 테케를 보면 이해 됨... 

'''
"ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"

개수가 적은 주문부터 탐색 (안해도 무방한가?)
-> 작은 집합에서부터 큰 집합으로 경우의 수를 따지기 
-> ex. AB나 CD의 조합이 다른 집합에도 있는지 확인 

dic = {
    2: [(1, ab)]
    ... 
}

1. ab 탐색 
    ab의 개수가 course 안에 있는지 확인 
    있다면, ab가 다른 집합에도 있는지 확인 
    그 개수를 카운트 
        abcde 안에 있음 => 1회 
    
    (주문 횟수, 단품명 오름차순으로) 를 현재 개수 2의 딕셔너리 값에 저장된 조합과 비교, 
        이것의 횟수가 더 높다면 교체
        횟수가 같다면 추가 
    (1, ab) 저장 
2. cd 탐색 
    cd의 개수가 course 안에 있음 
    cd가 abcde, acd 안에 있음 => 2회 
    기존에 저장되어 있던 (1, ab)의 1회보다 크기 때문에 교체
    (2, cd) 저장 
3. acd 탐색 
... 반복 
'''

'''
a: 4, 
b: 2, 
c: 3, 
d: 4, 
e: 2, 
x: 2, 
y: 2, 
z: 2

a: 1, 
x: 3, 
y: 2, 
z: 1, 
w: 2

x: 3, 
y: 2, 
w: 2

1번 ~ 3번 손님 
x: 1, 2, 3
y: 1, 2
z: 1
w: 2, 3
a: 3

x: 1, 2, 3
y: 1, 2
w: 2, 3

이건 set 함수 쓰기 
x, w => 2, 3번에게 공통으로 
x, y => 1, 2번에게 공통으로 

'''

def solution(orders, course):
    answer = []
    
    # 일단은 작은 집합에서 큰 집합으로 탐색 
    orders = sorted(orders, key = lambda x: len(x)) # 단품 개수를 기준으로 오름차순 정렬 
    print(orders)
    
    max_len = max(orders)
    
    dic = {}
    for c in course:
        dic[c] = []
        
    print(dic)
    
    for i in range(len(orders)):
        cur = orders[i]
        key = len(cur)
        
        if key not in course:
            continue
        cnt = 1 # 주문 횟수는 나 자신 포함 
        
        if len(cur) == max_len: # 이 구문은 없어도 될듯?? 
            break
        
        for j in range(i+1, len(orders)):
            near = orders[j]
            if len(cur) == len(near):
                continue
            # print(cur, near)
            
            # 비교 
            for c in cur:
                if c not in near:
                    break
            else:
                # 모두 속한다면 
                print(cur, near)
                cnt += 1
                
        # 탐색 끝 
        if dic[key]:
            # 카운트가 더 크다면 교체 
            if dic[key][0][0] < cnt:
                dic[key] = [(cnt, cur)]
            # 카운트가 같다면 추가 
            elif dic[key][0][0] == cnt:
                dic[key].append((cnt, cur))
        # 빈 배열이라면 추가 
        else:
            dic[key].append((cnt, cur))
            
        print(dic)
    
    return answer
"""