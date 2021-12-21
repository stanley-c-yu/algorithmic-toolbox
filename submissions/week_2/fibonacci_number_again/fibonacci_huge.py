# Uses python3
import sys

class Colossal_Fibonacci_Modulus(): 

    def calc_fib_fast(self, n):
        # Fast implementation for calculating the nth Fibonacci
        if (n <= 1):
            return n 
        
        F = [0, 1]
        for i in range(2, n + 1):
            F.append(F[i-1] + F[i - 2])
        return F[n]
        
    def get_fibonacci_huge_naive(self, args):
        # Naive method for calculating the mth modulus of the nth Fibonacci
        n = args[0]
        m = args[1]
        
        if n <= 1:
            return n

        previous = 0
        current  = 1

        for _ in range(n - 1):
            previous, current = current, previous + current

        return current % m
        
    def get_fibonacci_huge_fast(self, args):
        '''
        Calculates the modulo of the nth Fibonacci number for some integer m > 0.  
        
        Inputs:
            n:  the index of the nth Fibonacci number
            m:  the divisor
        Returns:
            The modulo of the nth Fibonnaci Number
        '''
        n = args[0]
        m = args[1]
        
        pisano_arr = [] 
        counter = 0 
        breaker = True
        while breaker == True:
            #print(counter)
            if len(pisano_arr) > 2:
                # Checks for a new Pisano Period by seeing if the last two modulos were 0 and then 1 
                if pisano_arr[counter-2] == 0 and pisano_arr[counter-1] == 1:
                    breaker = False 
                    break
            pisano_arr.append(self.calc_fib_fast(counter) % m)
            counter += 1 
        
        key = len(pisano_arr) - 2 
        smaller_index = n % key
        
        return self.calc_fib_fast(smaller_index) % m 
        
        
# if __name__ == '__main__':
    # input = sys.stdin.read();
    # n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))

