/*
완탐 
모든 경우의 수 
*/
let answer = -1
function recur(alpha, sel, target, idx) {
    answer += 1
    
    // 성공 
    if (sel.join("") === target) {
        return true
    }
    
    // 실패 
    if (sel.length === 5) {
        return false
    }
    
    for (let i = 0; i < alpha.length; i++) {
        sel.push(alpha[i])
        if (recur(alpha, sel, target, i+1)) return true
        sel.pop()
    }
}



function solution(word) {
    const alpha = ['A', 'E', 'I', 'O', 'U']
    recur(alpha, [], word, 0)
    return answer;
}