import unittest
import time
from random import seed
from random import randint 


from maximum_pairwise_product import max_pairwise_product_fast, max_pairwise_product_naive

class MaxPairwiseProductTestCase(unittest.TestCase): 
    """Tests for 'maximum_pairwise_product.py """
    
    def run_test(self, arr): 
        """ 
        Helper function that runs the fast and naive implementations using the provided array, 
        computes their results and processing times in seconds, and then asserts whether 
        the outputs are equal.  
        """
        start = time.perf_counter_ns()
        fast_result = max_pairwise_product_fast(arr)
        end = time.perf_counter_ns()
        print("The fast algorithm completed in ", str(end - start), " seconds.")
        
        start = time.perf_counter_ns()
        naive_result = max_pairwise_product_naive(arr)
        end = time.perf_counter_ns() 
        print("The naive algorithm completed in ", str(end - start), " seconds.")
        
        self.assertEqual(fast_result, naive_result) 
        print("Fast = ", str(fast_result), ".  Naive = ", str(naive_result), ".")

    
    def test_123_sorted_arr(self):
        """ Given a sorted array, can we find the maximum pairwise product? """
        arr = [1, 2, 3]
        self.run_test(arr)  

        
    def test_123_reversed(self):
        """ Given a simple reversed array, can we find the maximum pairwise product? """ 
        arr = [3, 2, 1] 
        self.run_test(arr) 
        
    def test_12345_scrambled(self):
        """ Given a scrambled array, can we compute the maximum pairwise product? """
        arr = [5, 2, 1, 3, 4]
        self.run_test(arr)
        
    def test_high_pair_sorted(self):
        """ 
        Given a sorted array where the largest pair consists of the same number, 
        and wherein that number is only listed twice, can we run both the fast and 
        naive implementation and still return the same result?
        """
        arr = [0, 1, 3, 7, 10, 12, 12]
        self.run_test(arr) 
        
    def test_high_pair_reversed(self): 
        """ 
        Given a reversed array where the largest pair consists of the same number, 
        and wherein that number is only listed twice, can we run both the fast and 
        naive implementation and still return the same result?  
        """
        arr = [12, 12, 10, 7, 3, 1, 0]
        self.run_test(arr) 
        
    def test_triple_high_scrambled(self): 
        """ 
        Given a scrambled array wherein the pairwise product is computed from a number
        that appears three times in the array, can both the naive and fast implementations
        arrive at the same solution?  
        """
        arr = [90, 45, 55, 65, 29, 30, 8, 11, 90]
        self.run_test(arr) 
        
    def test_overflow_fast(self): 
        """ 
        Given an array that contains a max pairwise product that is the result of one or more
        absurdly large integers, will the naive and fast implementions return the expected result?  
        Will they return the same result?  
        """
        arr = [100000, 90000]
        self.assertEqual(max_pairwise_product_fast(arr), 9000000000)
        print("Overflow test for fast implementation has passed.")
        
    def test_overflow_naive(self): 
        arr = [100000, 90000]
        self.assertEqual(max_pairwise_product_naive(arr), 9000000000)
        print("Overflow test for naive implementation has passed.")
    
    def test_random(self): 
        """ 
        Given a randomly generated array of postive integers, will both the fast and naive 
        implementations arrive at the same solution?  
        """
        arr = []
        seed(1)
        for _ in range(1, 100): 
            value = randint(0, 999999999)
            arr.append(value)
        self.run_test(arr)
        
unittest.main()
        
        
        