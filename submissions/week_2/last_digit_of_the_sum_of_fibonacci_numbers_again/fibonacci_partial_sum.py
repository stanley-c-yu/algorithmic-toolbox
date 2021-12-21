# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def calc_fib_fast(n): 
    """ Fast implementation for calculating the nth Fibonacci """
    if n <= 1:
        return n    
    F = [0, 1] 
    for i in range(2, n + 1): 
        F.append(F[i-1] + F[i-2])
    return F[n]
    
def calculate_pisano(m = 10): 
    """ Calculates the Pisano Period for a value of m, and returns an array of the Period and the length of the period.  """
    pisano_arr = [] 
    counter = 0
    while True: 
        if len(pisano_arr) > 2: 
            # Checks for a new Pisano Period by seeing if the last two modulos were 0 and then 1 
            if pisano_arr[counter-2] == 0 and pisano_arr[counter-1] == 1:
                break
        pisano_arr.append(calc_fib_fast(counter) % m)
        counter += 1 
    
    #better_index = len(pisano_arr - 2) 
    
    return pisano_arr[0:(len(pisano_arr) - 2)]


def fibonacci_partial_sum_fast(from_, to):  
    """ Returns the last digit of the summation of all Fibonacci numbers from m to n. """
    pisano_arr = calculate_pisano() 
    idx_lo = from_ % len(pisano_arr)
    idx_hi = to % len(pisano_arr) 
    pseudo_sum = sum(pisano_arr[idx_lo:idx_hi+1])
    return pseudo_sum % 10 

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
