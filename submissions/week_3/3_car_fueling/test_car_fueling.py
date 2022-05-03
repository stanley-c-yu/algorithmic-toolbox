import unittest
import time 

from car_fueling import compute_min_refills

class CarFuelingTest(unittest.TestCase):
    
    def run_test(self, function, distance, tank, stops, expected_output):
        start = time.perf_counter_ns()
        self.assertEqual(function(distance, tank, stops), expected_output) 
        end = time.perf_counter_ns()
        print("The algorithm completed in ", str(end - start), " seconds.")

    def test_one(self): 
        self.run_test(compute_min_refills, 950, 400, [200, 375, 550, 750], 2)
        
    def test_two(self): 
        self.run_test(compute_min_refills, 10, 3, [1, 2, 5, 9], -1)
        
    def test_three(self): 
        self.run_test(compute_min_refills, 200, 250, [100,150], 0)
        
        
unittest.main()