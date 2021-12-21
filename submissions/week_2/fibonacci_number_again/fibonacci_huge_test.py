import unittest
import time

from fibonacci_huge import Colossal_Fibonacci_Modulus
from test_template import TemplateTestCase

cfm = Colossal_Fibonacci_Modulus()

class FibonacciTestCase(TemplateTestCase): 
    """Tests for fibonacci_huge.py """
    
    def __init__(self): 
        """ Initialize attributes of the parent class. """
        super().__init__()
        
    def test_example_one(self): 
        """
        For the 2015th Fibonacci Number, can we return the correct answer, 
        that F2015 mod 3 = 1?
        """
        self.run_test(cfm.get_fibonacci_huge_fast, cfm.get_fibonacci_huge_naive, 2015, 3)        
        
    def test_sample_one(self): 
        """ 
        For the 239th Fibonacci Number, can we return the correct answer, 
        that F239 mod 1000 = 161?  
        """
        self.run_test(cfm.get_fibonacci_huge_fast, cfm.get_fibonacci_huge_naive, 239, 1000)
        
    def test_sample_two(self):
        """ 
        For the 2,816,213,588th Fibonacci Number, can we return the correct answer,
        that Fn mod 239 = 151? 
        """
        #self.run_test(cfm.get_fibonacci_huge_fast, cfm.get_fibonacci_huge_naive, 2816213588, 239)
        self.run_single_method_test(cfm.get_fibonacci_huge_fast, 151, 2816213588, 239)

    def run_all_tests(self): 
        """ 
        Run all tests.  
        """
        self.test_example_one()
        self.test_sample_one()
        self.test_sample_two()
        self.stress_test(num_tests = 100, a_limit = 10000, b_limit = 1000, a_low = 1, b_low = 2, method_fast = cfm.get_fibonacci_huge_fast, method_naive = cfm.get_fibonacci_huge_naive)
        
    # def test_random(self):
        # # Runs a series of tests on 100 randomly chosen integers between the range 0 and 500. 
        # print("Starting stress test.")
        # arr_a = []
        # arr_b = [] 
        # print("Generating array of random integers in the range 0 to 500.")
        # for i in range(0, 100):
            # rand_integer_a = randint(0, 500)
            # rand_integer_b = randint(0, 500)
            # arr_a.append(rand_integer_a)
            # arr_b.append(rand_integer_b)
        # print("Done.") 

        # print("Testing 100 randomly generated integers in the range 0 to 500.")
        # for i in range(0, len(arr_a)): 
            # print("Evaluating the fast against the naive implementation of LCM when a = " + str(arr_a[i]) + " and b = " + str(arr_b[i]) + ".")
            # self.run_test(arr_a[i], arr_b[i])
            # print("Done.")
            # time.sleep(1)
        # print("Tests complete.")
        
#unittest.main()
ftc = FibonacciTestCase()
ftc.run_all_tests()
        
        
        