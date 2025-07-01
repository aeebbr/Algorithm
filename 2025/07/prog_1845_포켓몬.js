/*
경우의 수를 카운트하는 게 아니라, 요구사항에 맞을 때의 종류 번호를 리턴하는 것 

맵 정렬: value 기준 내림차순(=> 후반부 카운트가 금방 0이 되기 때문에, value가 0이라면 그 뒤는 탐색X)
맵을 차례대로 순회하면서 해당하는 종류 카운트 -1, limit 마리 수도 -1
마리 수가 0인 종류는 continue
limit가 0이 되면 종료 
*/
function solution(nums) {    
    let cntMap = new Map()
    
    nums.forEach((n) => {
        if (cntMap.get(n)) {
            cntMap.set(n, cntMap.get(n)+1)
        } else {
            cntMap.set(n, 1)
        }
    })
    
    let mapToArray = [...cntMap]

    mapToArray.sort((a, b) => b[1]-a[1])
    
    cntMap = new Map(mapToArray)
    
    let limit = nums.length / 2
    let selKind = new Set()
    
    while (limit > 0) {
        for (let [key, value] of cntMap) {
            if (limit === 0 || value === 0) {
                break 
            }
            
            // 선택 
            cntMap.set(key, value-1)
            limit -= 1
            selKind.add(key)
        }
    }
        
    return selKind.size;
}