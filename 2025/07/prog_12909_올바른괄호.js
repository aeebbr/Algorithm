function solution(s){
    let stack = []
    
    for (let i=0; i < s.length; i++) {
        const ss = s[i]
        
        if (ss === '(') {
            stack.push(true)
        } else {
            if (stack.length === 0) {
                return false
            }
            
            stack.pop()
        }
    }
    
    if (stack.length !== 0) {
        return false
    }

    return true;
}