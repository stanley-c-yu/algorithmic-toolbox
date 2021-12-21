import unittest
import time
from random import seed
from random import randint 


from gcd import gcd_naive, gcd_fast

class FibonacciTestCase(unittest.TestCase): 
    """Tests for gcd.py """
    
    def run_test(self, a, b): 
        """ 
        Helper function that runs the fast and naive implementations using the provided integer 'n', 
        computes their results and processing times in seconds, and then asserts whether 
        the outputs are equal.  
        """
        start = time.perf_counter_ns()
        fast_result = gcd_fast(a, b)
        end = time.perf_counter_ns()
        print("The fast algorithm completed in ", str(end - start), " seconds.")
        
        start = time.perf_counter_ns()
        naive_result = gcd_naive(a, b)
        end = time.perf_counter_ns() 
        print("The naive algorithm completed in ", str(end - start), " seconds.")
        
        self.assertEqual(fast_result, naive_result) 
        print("Fast = ", str(fast_result), ".  Naive = ", str(naive_result), ".")
        
    def test_18_35(self): 
        # Should evaluate to 1 when a = 18 and b = 35
        print("Evaluating the GCD of 18 and 35.  Expected result is 1. ")
        self.run_test(18, 35)
        print("Test complete.")
        
    def test_two_high(self):
        # Should evaluate to 17657 when a = 28851538 and b = 1183019
        print("Evaluating the GCD of 28851538 and 1183019.  Expected result is 17657.")
        self.run_test(28851538, 1183019)
        print("Test complete.")        
        
    def test_random(self):
        # Runs a series of tests on 100 randomly chosen integers between the range 0 and 99999999. 
        print("Starting stress test.")
        arr_a = []
        arr_b = [] 
        print("Generating array of random integers in the range 0 to 99999999.")
        for i in range(0, 100):
            rand_integer_a = randint(0, 99999999)
            rand_integer_b = randint(0, 99999999)
            arr_a.append(rand_integer_a)
            arr_b.append(rand_integer_b)
        print("Done.") 

        print("Testing 100 randomly generated integers in the range 0 to 99999999.")
        for i in range(0, len(arr_a)): 
            print("Evaluating the fast against the naive implementation of GCD when a = " + str(arr_a[i]) + " and b = " + str(arr_b[i]) + ".")
            self.run_test(arr_a[i], arr_b[i])
            print("Done.")
            time.sleep(1)
        print("Tests complete.")
        
unittest.main()
        
        
        