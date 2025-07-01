/*
스택 
탑과 현재를 비교해서 동일한 게 나오면 그건 푸쉬하지 않음 
*/
function solution(arr)
{
    let stack = [arr[0]]
    
    for (let i=1; i < arr.length; i++) {
        let cur = arr[i]
        let top = arr[i-1]
       
        if (top !== cur) {
            stack.push(cur)        
        }
    }

    return stack;
}