const fib = require("./fibonacci"); 

test("Tests if my Fibonacci algorithm can correctly and efficiently compute 10th Fibonacci as 55:", () => {
	expect(fib(10)).toBe('55');
});

test("Tests if my Fibonacci algorithm can correctly and efficiently compute the 14th Fibonacci as 377:", () => {
	expect(fib(14)).toBe('377');
});

test("Tests if my Fibonacci algorithm can correctly and efficiently compute the 20th Fibonacci as 6765:", () => {
	expect(BigInt(fib(20))).toBe(BigInt(6765));
});

test("Can it handle the 150th Fibonacci? (can it handle ridiculously large numbers?)", () => {
	expect(fib(150)).toBe('9.9692166771893033862144057602e+30');
});