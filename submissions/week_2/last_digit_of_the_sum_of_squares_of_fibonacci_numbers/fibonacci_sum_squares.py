# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

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
    
    
def fibonacci_sum_squares_fast(n): 
    pisano_arr = calculate_pisano() 
    height_idx = n % len(pisano_arr) 
    width_idx = (n + 1) % len(pisano_arr)
    area_last_digit = ( pisano_arr[height_idx] * pisano_arr[width_idx] ) % 10
    return area_last_digit

# print(fibonacci_sum_squares_fast(7))


# if __name__ == '__main__':
    # n = int(stdin.read())
    # print(fibonacci_sum_squares_fast(n))
