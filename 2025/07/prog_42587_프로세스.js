/*
a, b, c, d
2, 1, 3, 2
=> <2> // 1, 3, 2, 2
=> <1> // 3, 2, 2, 1
=> <3> !!c // 2, 2, 1 
=> <2> !!d // 2, 1
=> <2> !!a // 1
=> <1> !!b 
*/
function solution(priorities, location) {
    var answer = 0;
    let q = []
    
    priorities.forEach((p, i) => {
        let isTarget = false
        if (i === location) isTarget = true
        q.push([p, isTarget])
    })
        
    priorities.sort()    
    
    while (q.length > 0) {
        const [front, isTarget] = q[0]
        const maxPri = priorities[priorities.length-1]
                
        q.splice(0, 1)

        // 다시 넣기 
        if (front !== maxPri) {
            q.push([front, isTarget])
            continue
        }
        
        // 프로세스 실행 
        answer += 1
                
        // 타겟이라면 
        if (isTarget) break
        
        priorities.pop()
    }
    
    
    return answer;
}