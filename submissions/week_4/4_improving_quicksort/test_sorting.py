import unittest 
from sorting import randomized_quick_sort,nonrandomized_quick_sort, partition3

class TestQuickSort(unittest.TestCase):
        
    def test_partition_pivot_is_2(self): 
        # Pivot is 2, array after pivot chosen and moved to left is identical to original
        print("----------------")
        print("Test: Pivot is 2")
        result = partition3(arr = [2, 3, 9, 2, 2], l = 0, r = 4, index = False)
        self.assertEqual(result, [2, 2, 2, 9, 3])

    def test_partition_pivot_is_3(self):
        # Pivot is 3 
        print("----------------")
        print("Test: Pivot is 3")
        result = partition3(arr = [3, 2, 9, 2, 2], l = 0, r = 4, index = False)
        self.assertEqual(result, [2, 2, 2, 3, 9])

    def test_partition_pivot_is_9(self):
        # Pivot is 9 
        print("----------------")
        print("Test: Pivot is 9")
        result = partition3(arr = [9, 3, 2, 2, 2], l = 0, r = 4, index = False)
        self.assertEqual(result, [3, 2, 2, 2, 9])

    def test_partition_pivot_is_1(self): 
        # Pivot is 1 
        print("----------------")
        print("Test: Pivot is 1")
        result = partition3(arr = [1, 0, 2, 0, 2, 1, 1], l = 0, r = 6, index = False)
        self.assertEqual(result, [0, 0, 1, 1, 1, 2, 2])

    def test_partition_pivot_is_0(self):
        # Pivot is 0 
        print("----------------")
        print("Test: Pivot is 0")
        result = partition3(arr = [0, 1, 2, 0, 2, 1, 1], l = 0, r = 6, index = False)
        self.assertEqual(result, [0, 0, 2, 2, 1, 1, 1])

    def test_partition_index_return_pivot_is_2(self):
        # Pivot is 2, test if we return the correct indices of the pivot segment 
        print("----------------")
        print("Test: Pivot is 2 and testing for correct pivot indices returned")
        result = partition3(arr = [2, 3, 9, 2, 2], l = 0, r = 4, index = True)
        self.assertEqual(result, (0, 2))

    def test_partition_index_return_pivot_is_3(self):
        # Pivot is 3, test if we return the correct indices of the pivot segment 
        print("----------------")
        print("Test: Pivot is 3 and test for correct pivot indices returned")
        result = partition3(arr = [3, 2, 9, 2, 2], l = 0, r = 4, index = True)
        self.assertEqual(result, (3, 3))

    def test_partition_index_return_pivot_is_9(self):
        # Pivot is 9, test if we return the correct indices of the pivot segment
        print("----------------")
        print("Test: Pivot is 9 and test for correct pivot indices returned")
        result = partition3(arr = [9, 3, 2, 2, 2], l = 0, r = 4, index = True)
        self.assertEqual(result, (4, 4))

    def test_partition_index_return_pivot_is_0(self):
        # Pivot is 0, test if we return the correct indices of the pivot segment
        print("----------------")
        print("Test: Pivot is 0 and test for correct pivot indices returned")
        result = partition3(arr = [0, 1, 2, 0, 2, 1, 1], l = 0, r = 6, index = True)
        self.assertEqual(result, (0, 1))
        
    def test_correct_above_below_partition_pivot_is_2(self):
        # Pivot is 2 for array [2, 3, 9, 2, 2].  Verifying correct return of Left of Pivot and Right of Pivot arrays 
        print("----------------")
        print("Test: Pivot is 2 and verifying correct Left Of and Right Of Partitions returned.")
        result = nonrandomized_quick_sort(a = [2, 3, 9, 2, 2], l = 0, r = 4, index = True, return_partitions = True)
        self.assertEqual(result, ([], [9, 3]))

    def test_correct_above_below_partition_pivot_is_3(self):
        # Pivot is 3 for array [3, 2, 9, 2, 2].  Verifying correct return of Left of Pivot and Right of Pivot arrays 
        print("----------------")
        print("Test: Pivot is 3 and verifying correct Left Of and Right Of Partitions returned.")
        result = nonrandomized_quick_sort(a = [3, 2, 9, 2, 2], l = 0, r = 4, index = True, return_partitions = True)
        self.assertEqual(result, ([2, 2, 2], [9]))
        
    def test_correct_above_below_partition_pivot_is_9(self):
        # Pivot is 9 for array [9, 3, 2, 2, 2].  Verifying correct return of Left of Pivot and Right of Pivot arrays
        print("----------------")
        print("Test: Pivot is 9 and verifying correct Left Of and Right Of Partitions returned.")
        result = nonrandomized_quick_sort(a = [9, 3, 2, 2, 2], l = 0, r = 4, index = True, return_partitions = True)
        self.assertEqual(result, ([3, 2, 2, 2], []))
        
    def test_correct_above_below_partition_pivot_is_1(self): 
        # Pivot is 1 for array [1, 0, 2, 0, 2, 1, 1].  Verifying correct return of Left of Pivot and Right of Pivot arrays
        print("----------------")
        print("Test: Pivot is 1 and verifying correct Left Of and Right Of Partitions returned.")
        result = nonrandomized_quick_sort([1, 0, 2, 0, 2, 1, 1], l = 0, r = 6, index = True, return_partitions = True)
        self.assertEqual(result, ([0, 0], [2, 2]))
        
    def test_correct_above_below_partition_pivot_is_0(self):
        # Pivot is 0 for array [0, 1, 2, 0, 2, 1, 1].  Verifying correct return of Left of Pivot and Right of Pivot arrays
        print("----------------")
        print("Test: Pivot is 0 and verifying correct Left Of and Right Of Partitions returned.")
        result = nonrandomized_quick_sort(a = [0, 1, 2, 0, 2, 1, 1], l = 0, r = 6, index = True, return_partitions= True)
        self.assertEqual(result, ([], [2, 2, 1, 1, 1]))
        
unittest.main() 