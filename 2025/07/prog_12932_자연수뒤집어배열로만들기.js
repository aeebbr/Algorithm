function solution(n) {
    var answer = [];
    n = String(n)
        
    for (let i = n.length-1; i > -1 ; i--) {
        answer.push(Number(n[i]))
    }
    
    return answer;
}