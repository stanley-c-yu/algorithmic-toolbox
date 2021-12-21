import unittest 
from fibonacci_partial_sum import fibonacci_partial_sum_naive, fibonacci_partial_sum_fast 

class FibonacciTestCase(unittest.TestCase): 
    """ Tests for fibonacci_partial_sum.py """
    
    def test_sample_one(self): 
        self.assertEqual(fibonacci_partial_sum_fast(3, 7), 1)
        
    def test_sample_two(self): 
        self.assertEqual(fibonacci_partial_sum_fast(10, 10), fibonacci_partial_sum_naive(10,10))
        
    def test_sample_three(self): 
        self.assertEqual(fibonacci_partial_sum_fast(10, 200), fibonacci_partial_sum_naive(10, 200))
        
unittest.main()