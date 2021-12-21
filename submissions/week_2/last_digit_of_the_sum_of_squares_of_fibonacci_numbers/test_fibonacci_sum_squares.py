import unittest 
from fibonacci_sum_squares import fibonacci_sum_squares_naive, fibonacci_sum_squares_fast


class FibonacciTestCase(unittest.TestCase): 
    """ Test cases for fibonacci_sum_squares.py """
    
    def test_sample_one(self): 
        print("Running first test case")
        self.assertEqual(fibonacci_sum_squares_fast(7), 3)
        print("Done.")
        
    def test_sample_two(self): 
        print("Running second test case")
        self.assertEqual(fibonacci_sum_squares_fast(73), 1)
        print("Done.")
        
    def test_sample_three(self): 
        print("Running third test case")
        self.assertEqual(fibonacci_sum_squares_fast(1234567890), 0)
        print("Done.")

unittest.main()        