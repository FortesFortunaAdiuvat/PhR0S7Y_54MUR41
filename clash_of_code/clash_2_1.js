var inputs = readline().split(' ');
const N = parseInt(inputs[0]);
const M = parseInt(inputs[1]);
const S = parseInt(readline());
let blocks = 0
for (let i = 0; i < N; i++) {
    const row = readline().match(/o/g) || []
    blocks += row.length
}

console.log(blocks*S);