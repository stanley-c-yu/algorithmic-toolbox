import unittest
from binary_search import BinarySearch

search = BinarySearch() 

class TestBinarySearch(unittest.TestCase):
    def test_not_found(self):
        for keys in ([], [1], [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16]):
            for target in (0, 4, 14, 17):
                self.assertEqual(search.left_finder(keys, target), -1)
                self.assertEqual(search.right_finder(keys, target), -1)
                self.assertListEqual(search.duplicate_binary_search(keys, target), [])

    def test_single_found(self):
        for keys in ([1], [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16]):
            for pos, target in enumerate(keys): # note, use enumerate in place of a user-defined counter variable
                #print(pos, target)
                self.assertEqual(search.left_finder(keys, target), pos)
                self.assertEqual(search.right_finder(keys, target), pos)
                self.assertEqual(search.duplicate_binary_search(keys, target), [pos])

    def test_left_right_and_range_for_embedded_sequence_v1_found(self):
        keys = [1, 13, 42, 42, 42, 77, 78]
        target = 42
        self.assertEqual(search.left_finder(keys, target), 2)
        self.assertEqual(search.right_finder(keys, target), 4)
        self.assertListEqual(search.duplicate_binary_search(keys, target), [2, 3, 4])

    def test_left_right_and_range_for_embedded_sequence_v2_found(self): 
        keys = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6]
        target = 4
        self.assertEqual(search.left_finder(keys, target), 3)
        self.assertEqual(search.right_finder(keys, target), 5)
        self.assertListEqual(search.duplicate_binary_search(keys, target), [3, 4, 5])

    def test_left_right_and_range_for_embedded_sequence_v3_found(self):
        keys = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6]
        target = 5
        self.assertEqual(search.left_finder(keys, target), 6)
        self.assertEqual(search.right_finder(keys, target), 7)
        self.assertListEqual(search.duplicate_binary_search(keys, target), [6, 7])

    def test_left_right_and_range_for_sequence_beginning_at_index_0_found(self):
        # Left most is first element
        keys = [1, 1, 1, 4, 4, 4, 5, 5, 6, 6, 6]
        target = 1
        self.assertEqual(search.left_finder(keys, target), 0)
        self.assertEqual(search.right_finder(keys, target), 2)
        self.assertListEqual(search.duplicate_binary_search(keys, target), [0, 1, 2])

    def test_left_right_and_range_for_sequence_ending_at_last_index_found(self):
        # Right most is last element
        # This test currently fails to realize 10 as right most
        keys = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6]
        target = 6
        self.assertEqual(search.left_finder(keys, target), 8)
        self.assertEqual(search.right_finder(keys, target), 10)
        self.assertListEqual(search.duplicate_binary_search(keys, target), [8, 9, 10])

    def test_duplicate_in_middle(self):
        target = 4
        for keys, expected in (
            ([1, 4, 4, 7], [1, 2]),
            ([1, 4, 4, 4, 4, 4, 4, 4, 7], [1, 2, 3, 4, 5, 6, 7]),
            ([1, 2, 3, 4, 4, 4, 5, 6, 7], [3, 4, 5]),
        ):
            self.assertTrue(search.double_recursive_binary_search(keys, target) in expected)
            self.assertEqual(search.left_finder(keys, target), expected[0])
            self.assertEqual(search.right_finder(keys, target), expected[-1])
            self.assertListEqual(search.duplicate_binary_search(keys, target), expected)
        
unittest.main()