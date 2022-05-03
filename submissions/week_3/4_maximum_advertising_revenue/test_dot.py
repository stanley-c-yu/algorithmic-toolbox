import unittest
from dot_product import max_dot_product 

class TestMaxDotProduct(unittest.TestCase): 
    
    def test_one_slot(self): 
        a = [23]
        b = [39]
        self.assertEqual(max_dot_product(a,b), 897)
        
    def test_three_slots(self): 
        a = [1, 3, -5]
        b = [-2, 4, 1] 
        self.assertEqual(max_dot_product(a,b,), 23)
        
    def test_opposite_orders(self): 
        a = [-1, 3, 5, 77, 102]
        b = [777, 666, 69, 55, -5]
        self.assertEqual(max_dot_product(a,b), 131051) 
        

unittest.main()