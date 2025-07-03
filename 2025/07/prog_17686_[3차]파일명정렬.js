function solution(files) {
    var answer = [];
    let total = []
    
    for (let i=0; i < files.length; i++) {
        const file = files[i].split("")
        const origin = files[i]
        // 헤드, 넘버, 테일 나누기 
        
        // 헤드 나누기
        let head = ""
        while (file.length > 0) {
            const f = file[0]
            // 숫자라면 
            if (f >= '0' && f <= '9') {
                break
            }
            head += f
            file.shift()
        }
                
        // 넘버 나누기 
        let number = ""
        while (file.length > 0 && number.length < 5) {
            const f = file[0] 
            // 숫자 -> false, 문자 -> true
            // 숫자가 아니라면 
            if (!(f >= '0' && f <= '9')) {
                break
            }
            number += f.trim()
            file.shift()
        }
        
        total.push([origin, head, number])
    }
    
    // 정렬 
    total.sort((a, b) => {
        // 헤드가 같다면 숫자순 정렬
        if (a[1].toLowerCase() === b[1].toLowerCase()) {
            return Number(a[2]) - Number(b[2]) 
        }
        // 헤드 정렬 
        else {
            return a[1].toLowerCase().localeCompare(b[1].toLowerCase())
        }
    })
    
    total.forEach((t) => answer.push(t[0]))
    return answer;
}