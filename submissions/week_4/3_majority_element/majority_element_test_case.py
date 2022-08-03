import unittest 
from majority_element import get_majority_element 


class MajorityElementTestCases(unittest.TestCase):
    
    def test_arr_23922(self):
        '''Test array [2, 3, 9, 2, 2] for a majority of 2.'''
        self.assertEqual(get_majority_element([2, 3, 9, 2, 2], 0, 4), 2)
        
    def test_arr_1234(self): 
        '''Test array [1, 2, 3, 4] to determine absence of majority element'''
        self.assertEqual(get_majority_element([1, 2, 3, 4], 0, 3), -1)
        
    def test_arr_1231(self):
        '''Test array [1, 2, 3, 1] to determine absence of majority element'''
        self.assertEqual(get_majority_element([1, 2, 3, 1], 0, 3), -1)
        
unittest.main()