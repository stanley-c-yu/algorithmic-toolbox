// by Alexander Nikolskiy, Solution by Stanley Yu

const math = require('mathjs');
/* import { create, all } from 'mathjs';
const math = create(all); 
math.config({
  number: 'BigNumber',      // Default type of number:
                            // 'number' (default), 'BigNumber', or 'Fraction'
  precision: 64             // Number of significant digits for BigNumbers
}) */


/* const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
} */

function fib(n) {
    // write your code here
	// solution is a little hacky, relying on some weird bigint and string conversions 
	// to make sure the test cases even work properly.  Had to use math.format() to just 
	// get a single number returned and not an object, but it returns it as a string (hence strings in test cases).  
	// So between what I have and what I did in Python, I'm convinced I've got the basic idea right.  But definitely 
	// not something I'd like to submit as a final product.  Not without more work and consulting anyway.  
	const F = [0, 1]; 
	for (let i = 2; i < n + 1; i ++) {
		//F.push(F[i - 1] + F[i - 2]);
		F.push(math.add(math.bignumber(F[i - 1]), math.bignumber(F[i - 2])));
	}
	return math.format(F[n]);
}

module.exports = fib;
