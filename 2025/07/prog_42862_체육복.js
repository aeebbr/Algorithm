/*
lost를 기준으로 탐색 

1. 도난 학생이 여벌을 갖고 있다면 무조건 자신이 갖기 

각 도난 학생별로 여벌 받을 수 있는 학생 전부 매치하기 
2: [1, 3]
4: [3, 5]
=> 여벌 받을 수 있는 학생 수 적은 순서로 오름차순 정렬(값 기준)
=> 그 순서대로 배분하기 
*/
function solution(n, lost, reserve) {
    var answer = 0; 
    let cntMap = new Map()
    let reserveMap = new Map()
    
    reserve.forEach((r) => {
        reserveMap.set(r, true)
    })
    
    for (let i=0; i < lost.length; i++) {
        let cur = lost[i]
        
        cntMap.set(cur, [])
        const borrowStudent = cntMap.get(cur)
        const value = cntMap.get(cur)
        
        if (reserve.includes(cur)) {
            value.push(cur)
            cntMap.set(cur, value)
            continue
        } 
        if (reserve.includes(cur-1)) {
            const front = cur-1
            value.push(front)
            cntMap.set(cur, value)
        }
        if (reserve.includes(cur+1)) {
            const back = cur+1
            value.push(back)
            cntMap.set(cur, value)
        }
    }
    
    const cntArray = [...cntMap]
    // value 기준 오름차순 정렬 
    cntArray.sort((a, b) => a[1].length - b[1].length)    
    cntMap = new Map(cntArray)
    
    // 순차적으로 배분 
    for (let [key, value] of cntMap) {
        for (let cur of value) {
            const isAvail = reserveMap.get(cur)
            if (isAvail) {
                reserveMap.set(cur, false)
                answer += 1
                break
            }
        }
    }
    
    return answer + (n-lost.length);
}