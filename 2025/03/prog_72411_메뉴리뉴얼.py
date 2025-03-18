'''
<후보 조건> 
- 2가지 이상의 구성일 것 
- 2번 이상 주문된 구성일 것 
- cousre에 있는 개수의 구성일 것([2, 3, 5] => 단품이 각 2개, 3개, 5개로 구성된 코스. 4개로 구성된 것은 안됨)

중요!!! 단품의 개수가 같은 코스가 여러 개라면, 주문 순서가 최대인 코스들을 선택함 !!! 
'''
course_dic = {}
course_max_cnt_dic = {} # course의 각 원소값과 일치하는 코스의 최대 카운트 
def solution(orders, course):
    global course_max_cnt_dic
    def combi(arr, idx, max_course, order):
        global course_dic
        global course_max_cnt_dic
        
        if len(arr) in course:
            string = "".join(arr)
            
            if string in course_dic:
                course_dic[string] += 1
            else:
                course_dic[string] = 1
                
            course_max_cnt_dic[len(arr)] = max(course_max_cnt_dic[len(arr)], course_dic[string])
                
        # 기저조건: 길이가 course의 최대값이거나, order의 최대 길이라면 
        if len(arr) == max_course or idx == len(order):
            return 

        for i in range(idx, len(order)):
            arr.append(order[i])
            combi(arr, i+1, max_course, order)
            arr.pop()
    
    answer = []
    
    for c in course:
        course_max_cnt_dic[c] = 0

    for order in orders:
        combi([], 0, max(course), sorted(order)) # 정렬된 order 넘기기 
    
    for k, v in course_dic.items():
        max_cnt = course_max_cnt_dic[len(k)] # 같은 개수의 코스들 사이에서 최대 카운트
        if v >= 2 and v == max_cnt:
            answer.append(k)
    
    # 오름차순 정렬 
    answer.sort()
    return answer