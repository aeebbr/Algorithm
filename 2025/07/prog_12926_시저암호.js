function solution(s, n) {
    var answer = '';
    
    const small = Array(26).fill().map((_, i) => String.fromCharCode(i+97))
    const large = Array(26).fill().map((_, i) => String.fromCharCode(i+65))
    
    for (let i = 0; i < s.length; i++) {
        const cur = s[i]
        let idx = 0
        let next = ''
        
        if (cur === " ") {
            answer += " "
            continue
        }
        
        // 소문자라면 
        if (small.includes(cur)) {
            idx = small.indexOf(cur) 
            next = small[(idx+n) % 26] 
        } else {
            idx = large.indexOf(cur) 
            next = large[(idx+n) % 26]
        }
        
        answer += next
    }
    return answer;
}