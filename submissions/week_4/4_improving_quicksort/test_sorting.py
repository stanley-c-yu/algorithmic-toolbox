import unittest 
from sorting import randomized_quick_sort, partition3

class TestQuickSort(unittest.TestCase):

    def test_arr_2_3_9_2_2(self): 
        result = randomized_quick_sort(a = [2, 3, 9, 2, 2], l = 0, r = 4)
        self.assertEqual(result, [2, 2, 2, 3, 9])
        
    def test_arr_4_9_4_4_1_9_4_4_9_4_4_1_4(self):
        result = randomized_quick_sort(a = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4], l = 0, r = 12)
        self.assertEqual(result, [1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 9, 9, 9])
        
    def test_arr_1_88_12_16_88_88_88_12_88(self): 
        result = randomized_quick_sort(a = [1,88,12,16,88,88,88,12,88], l = 0, r = 8)
        self.assertEqual(result, [1, 12, 12, 16, 88, 88, 88, 88, 88])
        
unittest.main() 