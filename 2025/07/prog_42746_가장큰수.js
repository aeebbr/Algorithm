/*
문자열로 정렬 
6, 10, 2 => 6, 2, 10
3, 30, 34, 5, 9 => 9, 5, 34, 30, 3
*/
function solution(numbers) {  
    const strings = numbers.map((n) => String(n))
    strings.sort((a, b) => (b+a).localeCompare(a+b)) // 3+30=330, 30+3=303
    const result = strings.join("");
    
    return result[0] === "0" ? "0" : result;
}