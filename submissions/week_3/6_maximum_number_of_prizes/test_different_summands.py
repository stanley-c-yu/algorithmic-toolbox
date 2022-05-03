import unittest
from different_summands import optimal_summands 


class TestOptimalSummands(unittest.TestCase): 
    
    def test_one(self): 
        result = optimal_summands(6) 
        expected = [1,2,3]
        self.assertListEqual(result, expected)  
        
    def test_two(self): 
        result = optimal_summands(8)
        expected = [1,2,5]
        self.assertListEqual(result, expected) 
        
    def test_three(self): 
        result = optimal_summands(2) 
        expected = [2] 
        self.assertListEqual(result, expected) 
        
        
unittest.main() 