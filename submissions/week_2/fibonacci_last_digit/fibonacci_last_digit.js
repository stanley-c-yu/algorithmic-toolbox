// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
}

function fib(n) {
    // write your code here
	const F = [0, 1];
	for (let i = 2; i < n + 1; i++) {
		F.push( (F[i - 1] + F[i - 2]) % 10);
	}
}	return F[n] % 10; 

module.exports = fib;

