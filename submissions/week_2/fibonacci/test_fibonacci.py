import unittest
import time
from random import seed
from random import randint 


from fibonacci import calc_fib_naive, calc_fib_fast

class FibonacciTestCase(unittest.TestCase): 
    """Tests for fibonacci.py """
    
    def run_test(self, n): 
        """ 
        Helper function that runs the fast and naive implementations using the provided integer 'n', 
        computes their results and processing times in seconds, and then asserts whether 
        the outputs are equal.  
        """
        start = time.perf_counter_ns()
        fast_result = calc_fib_fast(n)
        end = time.perf_counter_ns()
        print("The fast algorithm completed in ", str(end - start), " seconds.")
        
        start = time.perf_counter_ns()
        naive_result = calc_fib_naive(n)
        end = time.perf_counter_ns() 
        print("The naive algorithm completed in ", str(end - start), " seconds.")
        
        self.assertEqual(fast_result, naive_result) 
        print("Fast = ", str(fast_result), ".  Naive = ", str(naive_result), ".")
        
    def test_n_is_10(self): 
        # Should evaluate to 55 when n = 10
        print("Evaluating fast Fibonacci against naive Fibonacci when n = 10.  Expected result is 55.")
        self.run_test(10)
        print("Test complete.")

    def test_random(self):
        # Runs a series of tests on 100 randomly chosen integers between the range 0 and 25.  
        arr = []
        print("Generating array of random integers in the range 0 to 25.")
        for i in range(0, 100):
            rand_integer = randint(0, 25)
            arr.append(rand_integer)
        print("Done.") 

        print("Testing 100 randomly generated integers in the range 0 to 25.")
        for i in arr: 
            print("Evaluating the fast against the naive implementation of Fibonacci when n = " + str(i) + ".")
            self.run_test(i)
            print("Done.")
        print("Tests complete.")
        
unittest.main()
        
        
        