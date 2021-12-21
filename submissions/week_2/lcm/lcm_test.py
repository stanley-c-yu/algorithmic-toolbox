import unittest
import time
from random import seed
from random import randint 


from lcm import lcm_naive, lcm_fast

class FibonacciTestCase(unittest.TestCase): 
    """Tests for lcm.py """
    
    def run_test(self, a, b): 
        """ 
        Helper function that runs the fast and naive implementations using the provided integer 'n', 
        computes their results and processing times in seconds, and then asserts whether 
        the outputs are equal.  
        """
        start = time.perf_counter_ns()
        fast_result = lcm_fast(a, b)
        end = time.perf_counter_ns()
        print("The fast algorithm completed in ", str(end - start), " seconds.")
        
        start = time.perf_counter_ns()
        naive_result = lcm_naive(a, b)
        end = time.perf_counter_ns() 
        print("The naive algorithm completed in ", str(end - start), " seconds.")
        
        self.assertEqual(fast_result, naive_result) 
        print("Fast = ", str(fast_result), ".  Naive = ", str(naive_result), ".")
        
    def test_6_8(self): 
        # Should evaluate to 24 when a = 6 and b = 8
        print("Evaluating the LCM of 6 and 8.  Expected result is 24. ")
        self.run_test(6, 8)
        print("Test complete.")
        
    def test_two_high(self):
        # Should evaluate to 1933053046 when a = 28851538 and b = 1183019
        print("Evaluating the LCM of 28851538 and 1183019.  Expected result is 1933053046.")
        fast_result = lcm_fast(28851538, 1183019)
        self.assertEqual(fast_result, 1933053046) 
        print("Fast result = " + str(fast_result) + ".")
        #self.run_test(28851538, 1183019)
        print("Test complete.")        
        
    def test_random(self):
        # Runs a series of tests on 100 randomly chosen integers between the range 0 and 500. 
        print("Starting stress test.")
        arr_a = []
        arr_b = [] 
        print("Generating array of random integers in the range 0 to 500.")
        for i in range(0, 100):
            rand_integer_a = randint(0, 500)
            rand_integer_b = randint(0, 500)
            arr_a.append(rand_integer_a)
            arr_b.append(rand_integer_b)
        print("Done.") 

        print("Testing 100 randomly generated integers in the range 0 to 500.")
        for i in range(0, len(arr_a)): 
            print("Evaluating the fast against the naive implementation of LCM when a = " + str(arr_a[i]) + " and b = " + str(arr_b[i]) + ".")
            self.run_test(arr_a[i], arr_b[i])
            print("Done.")
            time.sleep(1)
        print("Tests complete.")
        
unittest.main()
        
        
        