# Uses python3
def calc_fib_naive(n):
    # Naive implementation
    if (n <= 1):
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

#n = int(input())
#print(calc_fib_naive(n))


def calc_fib_fast(n):
    # Fast implementation 
    if (n <= 1):
        return n 
        
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i-1] + F[i - 2])
    return F[n]
    