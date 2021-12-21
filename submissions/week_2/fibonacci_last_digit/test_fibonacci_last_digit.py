import unittest
import time
from random import seed
from random import randint 


from fibonacci_last_digit import get_fibonacci_last_digit_naive, get_fibonacci_last_digit_fast

class FibonacciTestCase(unittest.TestCase): 
    """Tests for fibonacci.py """
    
    def run_test(self, n): 
        """ 
        Helper function that runs the fast and naive implementations using the provided integer 'n', 
        computes their results and processing times in seconds, and then asserts whether 
        the outputs are equal.  
        """
        start = time.perf_counter_ns()
        fast_result = get_fibonacci_last_digit_fast(n)
        end = time.perf_counter_ns()
        print("The fast algorithm completed in ", str(end - start), " seconds.")
        
        start = time.perf_counter_ns()
        naive_result = get_fibonacci_last_digit_naive(n)
        end = time.perf_counter_ns() 
        print("The naive algorithm completed in ", str(end - start), " seconds.")
        
        self.assertEqual(fast_result, naive_result) 
        print("Fast = ", str(fast_result), ".  Naive = ", str(naive_result), ".")
        
    def test_n_is_3(self): 
        # Should evaluate to 2 when n = 3
        print("Evaluating the last digit of the Fibonacci when n is 3 for both fast and naive implementations.  Expected result is 2.")
        self.run_test(3)
        print("Test complete.")
        
    def test_n_is_331(self):
        # Should evaluate to 9 when n = 331 
        print("Evaluating the last digit of the Fibonacci when n is 331 for both fast and naive implementations.  Expected result is 9.")
        self.run_test(331)
        print("Test complete.")
        
    def test_n_is_327305(self):
        # Should evaluate to 5 when n is 327305
        print("Evaluating the last digit of the Fibonacci when n is 327305 for both fast and naive implementations.  Expected result is 5.")
        self.run_test(327305)
        print("Test complete.")
        
    def test_random(self):
        # Runs a series of tests on 100 randomly chosen integers between the range 0 and 333333.  
        arr = []
        print("Generating array of random integers in the range 0 to 333333.")
        for i in range(0, 100):
            rand_integer = randint(0, 333333)
            arr.append(rand_integer)
        print("Done.") 

        print("Testing 100 randomly generated integers in the range 0 to 333333.")
        for i in arr: 
            print("Evaluating the fast against the naive implementation of Fibonacci when n = " + str(i) + ".")
            self.run_test(i)
            print("Done.")
            time.sleep(2)
        print("Tests complete.")
        
unittest.main()
        
        
        