function solution(msg) {
    var answer = [];

    let dict = new Map()
    for (let i=0; i < 26; i++) {
        let word = String.fromCharCode(i + 65);
        dict.set(word, i+1)
    }
        
    while (msg.length > 0) {
        let w = msg[0]
        let newW = msg[0]
        let idx = 0
        
        for (let i = 1; i < msg.length; i++) {
            const c = msg[i]
            
            // ka = k + a
            // kak = ka + k
            newW = w + c
            
            // 사전에 없다면 탈출해서 직전 w 값을 사전에 추가하기 
            if (!dict.get(newW)) {
                break                 
            }
                     
            // w = ka
            w = newW
            idx += 1
        }
        
        answer.push(dict.get(w))
        
        // w 제거 
        // 0 ~ idx-1까지 제거해야 하니 
        // idx ~ 마지막까지 남기면 됨 
        msg = msg.slice(idx+1)

        // msg가 남아있다면 
        if (msg.length > 0) {
            // 사전에 등록 
            dict.set(newW, dict.size+1)
            // console.log(newW, ": ", dict.size+1)
        }
    }
        
    return answer;
}