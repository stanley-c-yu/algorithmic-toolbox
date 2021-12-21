import unittest
import time
from random import seed
from random import randint 


class TemplateTestCase(unittest.TestCase): 
    """ Template test case class. """
    
    def run_test(self, method_fast, method_naive, *args): 
        """ 
        Helper function that runs the fast and naive implementations of an algorithms and then 
        compares their results and runtimes in seconds.  It attempts to determine whether 
        their outputs are equal for correctness.
        
        Inputs: 
            method_fast: the superior implementation that we want to test 
            method_naive: the naive implementation that we know works, and that we want to 
                compare against the fast method.  
            *args: an unspecified number of positional arguments that are collected in a tuple.  
                These arguments are meant to be supplied to the methods for their execution.  
        """
        print("Running test.")
        start = time.perf_counter_ns()
        fast_result = method_fast(args)
        end = time.perf_counter_ns()
        print("The fast algorithm completed in ", str(end - start), " seconds.")
        
        start = time.perf_counter_ns()
        naive_result = method_naive(args)
        end = time.perf_counter_ns() 
        print("The naive algorithm completed in ", str(end - start), " seconds.")
        
        self.assertEqual(fast_result, naive_result) 
        print("Fast = ", str(fast_result), ".  Naive = ", str(naive_result), ".")
        print("Test complete.") 
        
    def run_single_method_test(self, method, solution, *args): 
        """ 
        Function to run a test of a method against a supplied solution.  
        
        Best used when the naive implementation may take too long to compute during
        a standard two-method comparison test.  
        """
        print("Running test.")
        result = method(args)
        self.assertEqual(result, solution)
        print("Solution: ", str(result), ".") 
        print("Test complete.")
        
    def stress_test(self, num_tests, a_limit, b_limit, a_low, b_low, method_fast, method_naive): 
        """
        Runs a specified number of tests against randomized values within specified ranges. 
        """
        print("Starting stress test.") 
        arr_a = []
        arr_b = []
        print("Generating array of random integers.")
        for i in range(0, num_tests):
            rand_integer_a = randint(a_low, a_limit)
            rand_integer_b = randint(b_low, b_limit)
            arr_a.append(rand_integer_a)
            arr_b.append(rand_integer_b)
        print("Done.")
        
        print("Running stress tests.")
        for i in range(0, num_tests): 
            self.run_test(method_fast, method_naive, arr_a[i], arr_b[i])
            print("Done.")
            time.sleep(1)
        print("Tests complete.")