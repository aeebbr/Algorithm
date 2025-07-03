/*
이동하는 선은 점 -> 점 이동의 방향을 나타내는 것 
(0, 0) -> (0, 1) 이동하는 선 
이동 내역을 저장할 때 양방향 둘 다 저장 
*/
function solution(dirs) {
    let board = []
    // 가로 11, 세로 11임 
    for (let i=0; i<11; i++) {
        row = new Array(11).fill(0)
        board.push(row)
    }
    
    const moves = []
    const dirInfo = {U: 0, D: 1, R: 2, L: 3}
    // 상, 하, 우, 좌
    const dr = [-1, 1, 0, 0]
    const dc = [0, 0, 1, -1]
    let cr = 5
    let cc = 5
    
    for (let i = 0; i < dirs.length; i++) {
        const d = dirs[i]
        const dirIdx = dirInfo[d]
        const nr = cr + dr[dirIdx]
        const nc = cc + dc[dirIdx]
        
        // 조건 확인 
        if (0 <= nr && nr <= 10 && 0 <= nc && nc <=10) {
            moves.push(`${cr}${cc}${nr}${nc}`)
            moves.push(`${nr}${nc}${cr}${cc}`)
            cr = nr
            cc = nc
        }
    }
    
    const moveSet = new Set(moves)
    return moveSet.size / 2;
}