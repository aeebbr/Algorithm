function replaceSharp(s) {
    return s
      .replace(/C#/g, 'c')
      .replace(/D#/g, 'd')
      .replace(/F#/g, 'f')
      .replace(/G#/g, 'g')
      .replace(/A#/g, 'a');
}

function solution(m, musicinfos) {
    m = replaceSharp(m);
    let answer = [];

    for (let k = 0; k < musicinfos.length; k++) {
        let [start, end, title, melody] = musicinfos[k].split(",");
        const [startH, startM] = start.split(":").map(Number);
        const [endH, endM] = end.split(":").map(Number);
        const playMin = (endH * 60 + endM) - (startH * 60 + startM);

        const playedMelody = replaceSharp(melody);
        let fullMelody = playedMelody.repeat(Math.ceil(playMin / playedMelody.length)).slice(0, playMin);

        if (fullMelody.indexOf(m) !== -1) {
            answer.push([playMin, k, title]);
        }
    }

    // 1. 재생시간 내림차순, 2. 먼저 입력된 순
    answer.sort((a, b) => b[0] - a[0] || a[1] - b[1]);

    return answer.length ? answer[0][2] : "(None)";
}