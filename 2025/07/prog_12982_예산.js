function solution(d, budget) {
    var answer = 0;
    
    d.sort((a, b) => a - b)

    for (let i = 0; i < d.length; i++) {
        const cur = d[i]
        budget -= cur 
        
        // 실패 
        if (budget < 0) {a
            break 
        }
        answer += 1
        
        if (budget === 0) {
            break 
        }
    }
    
    return answer;
}