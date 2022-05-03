import unittest
import time

from change import get_change

class MoneyChangeTest(unittest.TestCase): 
    """ Tests for change.py """
    def run_test(self, function, input, expected_output): 
        start = time.perf_counter_ns()
        self.assertEqual(function(input), expected_output) 
        end = time.perf_counter_ns()
        print("The algorithm completed in ", str(end - start), " seconds.")
        
    def test_one(self): 
        # Given a value of 2, will we correctly determine that two coins comprise the minimum number of change? 
        self.run_test(get_change, 2, 2)
        
    def test_two(self): 
        # Given a value of 28, will we correctly determine that two coins comprise the minimum number of change?  
        self.run_test(get_change, 28, 6)
                
unittest.main()

