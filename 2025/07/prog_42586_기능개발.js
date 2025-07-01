/*
<어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.>

93: 7 남음, 7/1 => 7일 
30: 70 남음, 70/30 => 2+1 => 3일 
55: 45 남음, 45/5 => 9일 
=> [7일, 3일, 9일]

뒤의 것이 현재의 것보다 작거나 같다면, 같이 배포됨 
뒤의 것이 현재의 것보다 크다면, 그보다 더 뒤는 탐색하지 않음 

큐: 오늘 배포할 수 있는 것 
for 
    cur = 현재 남은 일 수 
    큐.push(cur)
    
    if cur > 큐.front
        // 같이 배포 끝 
        answer.push(큐 길이 - 1) 
        큐 초기화 
*/
function solution(progresses, speeds) {
    var answer = [];
    let q = []
    
    for (let i=0; i < progresses.length;i++) {
        const cur = Math.ceil((100-progresses[i]) / speeds[i])
        q.push(cur)
        const front = q[0]
        
        if (cur > front) {
            answer.push(q.length - 1)
            q = [cur]
        }
    }
    
    answer.push(q.length)
    return answer;
}