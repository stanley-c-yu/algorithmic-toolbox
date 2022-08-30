import unittest
from sorting import partition3, randomized_quick_sort

class TestQuickSort(unittest.TestCase):

    def test_partition_pivot_is_2(self): 
        # Pivot is 2, array after pivot chosen and moved to left is identical to original
        print("----------------")
        print("Test: Pivot is 2")
        left, right = partition3(arr = [2, 3, 9, 2, 2], l = 0, r = 4)
        self.assertEqual([left, right], [0, 2])

    def test_partition_pivot_is_3(self):
        # Pivot is 3 
        print("----------------")
        print("Test: Pivot is 3")
        left, right = partition3(arr = [3, 2, 9, 2, 2], l = 0, r = 4)
        self.assertEqual([left, right], [3, 3])

    def test_sort_arr_93222(self):
        print("----------")
        print("Testing for correct quick sort for array [9, 3, 2, 2, 2]")
        arr = [9, 3, 2, 2, 2]
        result = randomized_quick_sort(arr = arr, l = 0, r = len(arr) - 1)
        self.assertEqual(result, [2, 2, 2, 3, 9])

    def test_sort_arr_32911(self):
        print("----------")
        print("Testing for correct quick sort for array [3, 2, 9, 1, 1]")
        arr = [3, 2, 9, 1, 1]
        result = randomized_quick_sort(arr = arr, l = 0, r = len(arr) - 1)
        self.assertEqual(result, [1, 1, 2, 3, 9])

    def test_sort_arr_1020211(self):
        print("----------")
        print("Testing for correct quick sort for array [1, 0, 2, 0, 2, 1, 1]")
        arr = [1, 0, 2, 0, 2, 1, 1]
        result = randomized_quick_sort(arr = arr, l = 0, r = len(arr) - 1)
        self.assertEqual(result, [0, 0, 1, 1, 1, 2, 2])

unittest.main()        
        
