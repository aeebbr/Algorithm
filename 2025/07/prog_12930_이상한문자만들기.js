function solution(s) {
    var answer = '';
    let arr = s.split(" ")
    
    for (let i = 0; i < arr.length; i++) {
        const word = arr[i]
        for (let j = 0; j < word.length; j++) {
            let w = word[j]
            
            if (j % 2 === 0) {
               answer += w.toUpperCase() 
            } else {
               answer += w.toLowerCase()                 
            }
        }
        
        if (i !== arr.length-1) {
            answer += " "        
        }
    }
    
    return answer;
}