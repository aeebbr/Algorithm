/*
모든 카드는 가로가 길게 회전
*/
function solution(sizes) {    
    sizes.map((s) => {
        return s.sort((a, b) => b-a)
    })
        
    let wMax = 0
    let hMax = 0
    
    sizes.forEach(([w, h]) => {
        wMax = Math.max(wMax, w)
        hMax = Math.max(hMax, h)
    })
        
    return wMax * hMax;
}