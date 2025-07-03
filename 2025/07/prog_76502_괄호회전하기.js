function isRight(arr) {
    let stack = []
    const openB = {'(': 0, '{': 1, '[': 2, a: 3}
    const closeB = {')': 0, '}': 1, ']': 2}
    
    for (let a of arr) {
        if (a in openB) {
            stack.push(a)
        } else {
            if (stack.length === 0) {
                return false
            }
            
            const open = stack.pop()
            if (!(open in openB)) {
                return false
            }

            const openI = openB[open]
            const closeI = closeB[a]           
            
            if (openI !== closeI) {
                return false
            }
        }
    }
    
    if (stack.length !== 0) {
        return false
    }
    
    return true
}


function solution(s) {
    var answer = 0;
    let arr = s.split("")
    
    // 총 몇 번 쉬프트? 
    for (let i = 0; i < arr.length; i++) {
        // 쉬프트하기 
        const front = arr.shift()
        arr.push(front)
 
        if (isRight(arr)) answer += 1
    }
    
    return answer;
}