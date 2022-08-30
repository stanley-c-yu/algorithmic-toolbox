# Uses python3
import sys
import random

def partition3(arr, l, r, index): 
    '''
    Inputs:
        a: array of elements 
        l: the index of the leftmost element of the array, "a" 
        r: the index of the rightmost element of the array, "a" 
    Returns: 
        The left and right coordinates that mark the beginning and end of our "bulk" pivot  
    '''
    i = 0
    l_idx_cp = l 
    r_idx_cp = r
    pivot_val = arr[l]
    while i <= r_idx_cp:
        if arr[i] < pivot_val: 
            arr[i], arr[l_idx_cp] = arr[l_idx_cp], arr[i]
            l_idx_cp += 1
        elif arr[i] > pivot_val:
            arr[i], arr[r_idx_cp] = arr[r_idx_cp], arr[i]
            r_idx_cp -= 1 
            i -= 1
        i += 1 
    if index == True:
            print("Partitioned Array: ", arr)
            print("Left side of partition: ", l_idx_cp, "|", "Right side of partition: ", r_idx_cp)
            return l_idx_cp, r_idx_cp
    else:
        print("Partitioned Array: ", arr)
        return arr

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def nonrandomized_quick_sort(a, l, r, index, return_partitions):
    '''
    Debug version without randomization to ensure consistent test results with test cases.  
    '''
    if l >= r:
        return 
    mid_left_idx, mid_right_idx = partition3(a, l, r, index)    
    if return_partitions == True: 
        print("Left of Pivot Partition: ", a[l:mid_left_idx])
        print("Right of Pivot Partition: ", a[mid_right_idx + 1:r])
        return a[l:mid_left_idx], a[mid_right_idx + 1:r + 1]
    #use partition3
    randomized_quick_sort(a, l, mid_left_idx - 1)
    randomized_quick_sort(a, mid_right_idx + 1, r) 
    return a
    
def left_sided_quick_sort(a, l, r, index, return_partitions):
    if l >= r:
        return 
    mid_left_idx, mid_right_idx = partition3(a, l, r, index)    
    if return_partitions == True: 
        print("Left of Pivot Partition: ", a[l:mid_left_idx])
        print("Right of Pivot Partition: ", a[mid_right_idx + 1:r + 1])
        return a[l:mid_left_idx], a[mid_right_idx + 1:r + 1]
    #use partition3
    left_sided_quick_sort(a, l, mid_left_idx - 1, index, return_partitions)
    #randomized_quick_sort(a, mid_right_idx + 1, r) 
    return a
    
def right_sided_quick_sort(a, l, r, index, return_partitions):
    if l >= r:
        return 
    mid_left_idx, mid_right_idx = partition3(a, l, r, index)    
    if return_partitions == True: 
        print("Left of Pivot Partition: ", a[l:mid_left_idx])
        print("Right of Pivot Partition: ", a[mid_right_idx + 1:r])
        return a[l:mid_left_idx], a[mid_right_idx + 1:r]
    #use partition3
    #left_sided_quick_sort(a, l, mid_left_idx - 1, index, return_partitions)
    right_sided_quick_sort(a, mid_right_idx + 1, r, index, return_partitions) 
    return a    
        
def randomized_quick_sort(a, l, r, index, return_partitions):
    if l >= r:
        return 
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    mid_left_idx, mid_right_idx = partition3(a, l, r, index)
    if return_partitions == True: 
        print("Left of Pivot Partition: ", a[l:mid_left_idx])
        print("Right of Pivot Partition: ", a[mid_right_idx + 1:r + 1])
        return a[l:mid_left_idx], a[mid_right_idx + 1:r + 1]
    #use partition3
    randomized_quick_sort(a, l, mid_left_idx - 1, index, return_partitions)
    randomized_quick_sort(a, mid_right_idx + 1, r, index, return_partitions) 
    return a




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
