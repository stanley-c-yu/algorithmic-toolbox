import unittest 
from sorting import randomized_quick_sort, partition3, partition

class TestQuickSort(unittest.TestCase):

#    def test_arr_2_3_9_2_2(self): 
#        result = randomized_quick_sort(a = [2, 3, 9, 2, 2], l = 0, r = 4)
#        self.assertEqual(result, [2, 2, 2, 3, 9])
        
#    def test_arr_4_9_4_4_1_9_4_4_9_4_4_1_4(self):
#        result = randomized_quick_sort(a = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4], l = 0, r = 12)
#        self.assertEqual(result, [1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 9, 9, 9])
        
#    def test_arr_1_88_12_16_88_88_88_12_88(self): 
#        result = randomized_quick_sort(a = [1,88,12,16,88,88,88,12,88], l = 0, r = 8)
#        self.assertEqual(result, [1, 12, 12, 16, 88, 88, 88, 88, 88])
        
    def test_partition_pivot_is_2(self): 
        # Pivot is 2, array after pivot chosen and moved to left is identical to original
        result = partition(arr = [2, 3, 9, 2, 2], l = 0, r = 4)
        self.assertEqual(result, [2, 2, 2, 9, 3])

    def test_partition_pivot_is_3(self):
        # Pivot is 3 
        result = partition(arr = [3, 2, 9, 2, 2], l = 0, r = 4)
        self.assertEqual(result, [2, 2, 2, 3, 9])

    def test_partition_pivot_is_9(self):
        # Pivot is 9 
        result = partition(arr = [9, 3, 2, 2, 2], l = 0, r = 4)
        self.assertEqual(result, [3, 2, 2, 2, 9])

    def test_partition_pivot_is_1(self): 
        # Pivot is 1 
        result = partition(arr = [1, 0, 2, 0, 2, 1, 1], l = 0, r = 6)
        self.assertEqual(result, [0, 0, 1, 1, 1, 2, 2])

    def test_partition_pivot_is_0(self):
        # Pivot is 0 
        result = partition(arr = [0, 1, 2, 0, 2, 1, 1], l = 0, r = 6)
        self.assertEqual(result, [0, 0, 2, 2, 1, 1, 1])

unittest.main() 