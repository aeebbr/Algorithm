/*
접두사인 경우의 수를 카운트하는 게 아니라, 한 번이라도 접두어인지 확인하는 것 

정렬하기 
["119", "97674223", "1195524421"]	
=> ["119", "1195524421", "97674223"]	

앞의 원소가 뒤의 원소의 0부터 포함되는지 확인 
*/
function solution(phone_book) {
	phone_book.sort();

	for (let i = 0; i < phone_book.length - 1; i++) {
		const cur = phone_book[i];
		const curLen = phone_book[i].length;
		const next = phone_book[i + 1];

		if (cur === next.slice(0, curLen)) {
			return false;
		}
	}

	return true;
}
