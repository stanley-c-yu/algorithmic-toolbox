class BinarySearch(): 
    '''A collection of Binary Search Implementations for an algorithms assignment'''
    def circular_binary_search(self, keys, target):
        '''A while-loop implementation of binary search.'''
        start, end = 0, len(keys) - 1
        while start <= end:
            mp = start + (end - start) // 2
            if keys[mp] == target:
                return mp
            elif target < keys[mp]:
                end = mp - 1
            else:
                start = mp + 1
        return -1
        
    def recursive_binary_search(self, keys, target, start = 0, end = None):
        ''' A recursive implementation of binary search.'''
        end = end if end is not None else len(keys) - 1 
        mp = start + (end - start) // 2
        if end < start:
            return -1
        elif keys[mp] == target:
            return mp
        elif target < keys[mp]:
            end = mp - 1
        else:
            start = mp + 1
        return recursive_binary_search(keys, target, start, end)
             
    def double_recursive_binary_search(self, keys, target, start = 0, end = None):
        '''
        Searches the array, 'keys', for an integer, 'target'.  Each
        call of the method also takes a 'start' and 'end' argument,
        specifying the index to start and end the search on.

        If the target is found to be in the keys array, the index of
        its location is returned.  If not, a -1 is returned. 
        '''
        end = end if end is not None else len(keys) - 1  # If end is set to a default argument of 'None', then set it to the index of the last element in the array, 'keys'.
        if end < start:  # If the last element is smaller than the first, then the array becomes valid because it is not sorted.
            return -1
        mp = start + (end - start) // 2 # Calculate the midpoint
        if target == keys[mp]: # Is the target at mp?
            return mp
        elif target < keys[mp]: # target is below the mp
            return self.double_recursive_binary_search(keys, target, start = start, end = mp - 1)
        else:
            return self.double_recursive_binary_search(keys, target, start = mp + 1, end=end)

    def left_finder(self, keys, target, start = 0, end = None):
        '''
        Finds the first, aka leftmost, occurrence of the target
        in keys using a binary search implementation.
        '''
        end = end if end is not None else len(keys) - 1 
        if end < start: 
            return -1
        mp = start + (end - start) // 2
        if ((mp == 0 or keys[mp - 1] < target) and  keys[mp] == target):
            return mp
        elif target <= keys[mp]:
            return self.left_finder(keys, target, start = start, end = mp - 1)
        else:
            return self.left_finder(keys, target, start = mp + 1, end = end)

    def right_finder(self, keys, target, start = 0, end = None):
        '''Finds the last, aka rightmost, occurrence of target in keys.'''
        end = end if end is not None else len(keys) - 1 
        if end < start: 
            return -1 
        mp = start + (end - start) // 2
        if ((mp == len(keys)-1 or target < keys[mp + 1]) and keys[mp] == target): # ultimately it was my inability to define a proper stopping condition correctly
            return mp
        elif target < keys[mp]: 
            return self.right_finder(keys, target, start = start, end = mp - 1)
        else: 
            return self.right_finder(keys, target, start = mp+1, end = end)

    def duplicate_binary_search(self, keys, target):
        '''
        Uses left finder and right finder to return all occurrences of target in keys.
        
        Returns: If no occurrences are found, returns [].  If one occurrence is found,
        returns a list consisting of one element that is the index location of the target
        in keys.  If multiple occurrences are found, returns a list of all indices where
        the target may be found in keys.  
        '''
        # Find a value in keys that qualifies as a possible left, right
        left, right = self.left_finder(keys, target), self.right_finder(keys, target)
        # Check properties of values returned 
        assert left <= right # 'assert' is a test to determine if the provided condition is True.  If False, returns an AssertionError.
        assert (left == -1) == (right == -1)  # Catches situations in which left or right are returned as None?
        # Return range
        return [] if left == -1 else list(range(left, right + 1))  # returns an empty list if the target DNE, else returns a list of indices or just a list of one index

        
if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(BinarySearch().double_recursive_binary_search(input_keys, q), end=' ')
