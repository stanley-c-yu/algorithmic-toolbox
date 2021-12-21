import unittest
from random import seed
from random import randint 
from fibonacci_sum_last_digit import fibonacci_sum_naive, fibonacci_sum_fast

class TestFibonacciSumLastDigit(unittest.TestCase): 
    
    def test_sample_one(self): 
        """ Tests for the last digit of the sum of the first 3 Fibonacci numbers """
        print("Test: can the provided implementation correctly determine the last digit of the first 3 Fibonacci numbers as 4? ")
        print("Computed solution: ", str(fibonacci_sum_fast(3)), ".")
        self.assertEqual(fibonacci_sum_fast(3), 4)
        
        
    def test_sample_two(self): 
        """ Tests for the last digit of the sum of the first 100 Fibonacci numbers """
        print("Test: can the provided implementation correctly determine the last digit of the first 100 Fibonacci numbers as 5? ")
        print("Computed solution: ", str(fibonacci_sum_fast(100)), ".")
        self.assertEqual(fibonacci_sum_fast(100), 5)
        
    def test_rndm_one(self): 
        rand_int = randint(0, 500) 
        self.assertEqual(fibonacci_sum_fast(rand_int), fibonacci_sum_naive(rand_int)) 
        
    def test_rndm_two(self): 
        rand_int = randint(0, 500) 
        self.assertEqual(fibonacci_sum_fast(rand_int), fibonacci_sum_naive(rand_int)) 
        
    def test_rndm_three(self): 
        rand_int = randint(0, 500) 
        self.assertEqual(fibonacci_sum_fast(rand_int), fibonacci_sum_naive(rand_int)) 
        
unittest.main()