/*
스택: 지금까지 중에 큰 것만 

현재와 탑 비교해서, 현재가 더 크면 탑 제거, 현재 삽입 
*/
function solution(number, k) {
    let stack = []
    
    for (let n of number) {
        n = Number(n)        
        
        while (stack.length > 0 && k > 0) {
            let top = stack[stack.length-1]
            
            if (n > top) {
                stack.pop()
                k -= 1
            } 
            // 스택에 변동 없으면 끝 
            else {
                break 
            }
        }
        stack.push(n)
    }
        
    if (k > 0) {
        stack.splice(stack.length - k)
    }
    
    return stack.join("");
}