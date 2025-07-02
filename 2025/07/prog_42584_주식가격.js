function solution(prices) {
    var answer = []
    for (let i = prices.length-1; i > -1; i--) {
        answer.push(i)
    }
    
    let stack = []
    
    for (let curI = prices.length-1; curI > -1; curI--) {
        const cur = prices[curI]
        let isFind = false
        
        // 스택의 각 값 탐색 
        while (stack.length > 0) {
            let [top, topI] = stack[stack.length-1] 
            
            if (cur <= top) {
                stack.pop()
            } else if (cur > top) {
                answer[curI] = (topI - curI)
                isFind = true
                break
            } 
        }

        stack.push([cur, curI])
    }

    return answer;
}