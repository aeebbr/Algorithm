/*
다리를 건넌다 = 다리 위에 있다 

각 트럭은 다리를 건너는 데에 시간이 얼마나 걸리나?? 
=> bridge_length만큼 
=> 다리 길이 = bridge_length
=> 한 번에 bridge_length개만큼만 
=> 다리는 총 bridge_length칸 
=> 트럭 하나는 다리를 건널 때 bridge_length칸을 지나야 함 = bridge_length 시간이 걸림 

다리 = 큐

순차적으로 큐에 트럭 넣기(트럭무게, 다리에 머물러있는 시간 카운트 값)
매 시간마다 다음 트럭이 다리에 올라올 수 있는지 체크 

while 대기트럭 
    // 1시간에는 기존 삭제와 동시에 새 삽입이 가능함 
    if 큐의 front 카운트가 최대개수와 같다면 
        큐에서 삭제
        현재개수와 현재무게 갱신

    if 다리에 새 트럭을 넣었을 때 다리 최대개수, 최대무게를 모두 넘지 않는다면
        큐에 삽입
        대기트럭열에서 삭제
        현재개수와 현재무게 갱신
    
    전체 시간 카운트 + 1
    
    while 큐
        각 트럭 시간 카운트 + 1

// 다리 위 남은 트럭 처리하기 
// 다리 위 맨 뒤의 트럭이 앞으로 걸리는 시간이 다리가 비어지는 데 걸리는 시간임 
전체 시간 += (다리길이 - 큐의 마지막 원소의 시간)
*/
function solution(bridge_length, weight, truck_weights) {
    let bridgeQ = []
    let totalCnt = 0
    let totalWeight = 0
    let time = 0
    
    while (truck_weights.length > 0) {
        // 다리 맨 앞 트럭 제거 
        if (bridgeQ.length > 0) {
            let [frontWeight, frontTime] = bridgeQ[0]
            if (bridgeQ[0][1] === bridge_length) {
                bridgeQ.splice(0, 1)
                totalCnt -= 1
                totalWeight -= frontWeight
            }
        }
        
        let newTruck = truck_weights[0]
        
        // 새 트럭 추가 
        if ((totalCnt + 1) <= bridge_length && (totalWeight + newTruck) <= weight) {
            // [트럭무게, 다리에 머문 시간]
            bridgeQ.push([newTruck, 0])
            truck_weights.splice(0, 1)
            totalCnt += 1
            totalWeight += newTruck
        }
        
        time += 1
        
        bridgeQ.forEach((_, i) => {
            bridgeQ[i][1] += 1
        })
    }
    
    // 대기 트럭에 남은 트럭은 없지만, 다리 위에는 남은 트럭이 있음 
    time += (bridge_length - bridgeQ[bridgeQ.length-1][1])
    
    return time+1; // 다리가 완전히 비어진 시점도 카운트하기 때문에 + 1
}