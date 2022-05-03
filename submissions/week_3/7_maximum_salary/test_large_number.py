import unittest 
from largest_number import largest_number

class LargeNumberTestCase(unittest.TestCase): 

    def test_one(self): 
        digits = [23, 3]
        result = largest_number(digits) 
        expected = "323"
        self.assertEqual(result, expected) 
        
    def test_two(self): 
        digits = [21, 2]
        result = largest_number(digits) 
        expected = "221"
        self.assertEqual(result, expected) 
        
    def test_three(self): 
        digits = [9,4,6,1,9]
        result = largest_number(digits) 
        expected = "99641"
        self.assertEqual(result, expected) 
        
    def test_four(self): 
        digits = [23, 39, 92]
        result = largest_number(digits) 
        expected = "923923"
        self.assertEqual(result, expected) 

unittest.main()                