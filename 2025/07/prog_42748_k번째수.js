function solution(array, commands) {
    var answer = [];
    
    commands.forEach(([i, j, k], idx) => {
        let newArray = array.slice(i-1, j)
        newArray.sort((a, b) => a-b)
        answer.push(newArray[k-1])
    })
    
    return answer;
}