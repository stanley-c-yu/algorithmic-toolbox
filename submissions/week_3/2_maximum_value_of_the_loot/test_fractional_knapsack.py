import unittest
import time 

from fractional_knapsack import get_optimal_value

class FractionalKnapsackTest(unittest.TestCase):
    
    def run_test(self, function, capacity, weights, values, expected_output):
        start = time.perf_counter_ns()
        self.assertEqual(function(capacity, weights, values), expected_output) 
        end = time.perf_counter_ns()
        print("The algorithm completed in ", str(end - start), " seconds.")

    def test_one(self): 
        self.run_test(get_optimal_value, 50, [20, 50, 30], [60, 100, 120], 180.)
        
    def test_two(self): 
        self.run_test(get_optimal_value, 10, [30], [500], 166.6667)
        
        
unittest.main()