// 각 배열을 객체로 만들어서, (이름: 인원수) 쌍으로 구현
// 두 객체 비교하면서 participant의 인원수가 completion의 인원수와 맞지 않다면 해당 이름 리턴
// 한 명만 찾으면 됨
function solution(participant, completion) {
	var answer = "";

	let partMap = new Map(); // 참가자
	let comMap = new Map(); // 완주자

	participant.forEach((p) => {
		if (partMap.get(p)) {
			partMap.set(p, partMap.get(p) + 1);
		} else {
			partMap.set(p, 1);
		}
	});

	completion.forEach((p) => {
		if (comMap.get(p)) {
			comMap.set(p, comMap.get(p) + 1);
		} else {
			comMap.set(p, 1);
		}
	});

	for (let [key, value] of partMap) {
		// 완주자 인원수와 맞지 않다면
		if (comMap.get(key) !== value) {
			return key;
		}
	}

	return answer;
}
