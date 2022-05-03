import unittest
from covering_segments import optimal_points

class CollectingSignaturesTestCase(unittest.TestCase): 
    '''
    Methods for testing the Collecting Signatures problem.
    '''
    
    def test_one(self): 
        '''
        Test array [(1,3), (2,5), (3,6)]
        '''
        print("Test One")
        expected = [3]
        result = optimal_points([(1,3), (2,5), (3,6)])
        self.assertEqual(expected, result) 
        
    def test_two(self): 
        '''
        Test array [(4,7), (1,3), (2,5), (5,6)]
        '''
        print("Test Two")
        expected = [3, 6]
        result = optimal_points([(4,7), (1,3), (2,5), (5,6)])
        self.assertEqual(expected, result)
        

unittest.main()