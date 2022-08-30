# Uses python3
import sys
import random

def partition2(a, l, r):
    '''A simple, but slower operating parititon function.'''
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def partition3(arr, l, r): 
    '''
    Takes an array and sorts it into three partitions: 
    everything less than the pivot value, everything equal to the pivot value,
    and everything greater than the pivot value.
    
    Inputs: 
        arr: array of elements 
        l: the index of the left most element of arr.  
            The element at l is equal to a pivot randomly chosen by randomized quick sort.  
        r: the index of the right most element of arr 
    Returns:
        The left and right coordinates of the pivot segment.  
    '''
    i = l # this needs to be set equal to l and not 0, otherwise we run into indexing errors
    l_copy, r_copy = l, r
    pivot_value = arr[l] # the pivot value is randomly chosen by quick sort and swapped into the 'l' position 
    while i <= r_copy:
        if arr[i] < pivot_value:
            arr[i], arr[l_copy] = arr[l_copy], arr[i]
            l_copy += 1
        elif arr[i] > pivot_value:
            arr[i], arr[r_copy] = arr[r_copy], arr[i]
            r_copy -= 1 # we need to consistently shrink the area of operation to avoid doing unnecessary work.  
            i -= 1 # when this kind of swap happens, we need to remain "in place" for operations to continue properly  
        i += 1 
    return l_copy, r_copy 

def randomized_quick_sort(arr, l, r):
    '''Randomly chooses a pivot and then recursively sorts an array around the pivot.'''
    if l >= r: 
        return
    k = random.randint(l, r) # randomly choose an index that directly relates to the pivot value 
    arr[l], arr[k] = arr[k], arr[l] # swap the pivot value into the 'l' position
    pivot_start, pivot_end = partition3(arr, l, r) 
    randomized_quick_sort(arr, l, pivot_start - 1) # sort below-pivot-partition
    randomized_quick_sort(arr, pivot_end + 1, r) # sort above-pivot-partition
    return arr


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
