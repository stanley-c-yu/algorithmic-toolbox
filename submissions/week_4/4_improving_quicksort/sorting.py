# Uses python3
import sys
import random

# def partition3(a, l, r):
    # '''
    # Inputs:
        # a: array of elements 
        # l: the index of the leftmost element of the array, "a" 
        # r: the index of the rightmost element of the array, "a" 
    # Returns: 
        # The left and right coordinates that mark the beginning and end of our "bulk" pivot  
    # '''
    # #write your code here
    # l_element_copy = a[l] # copy the left element.  We're creating our pivot by trying to group elements idential to the leftmost value
    # l_idx_copy = l # copy of the index of the leftmost element 
    # r_idx_copy = r # copy of the index of the rightmost element
    # idx = l_idx_copy # integer that is used to reference elements from the array one by one, starting the from the left 
    # while idx < r_idx_copy: 
        # if a[idx] < l_element_copy: # if the current element we're looking at is less than the initial left most value, ... 
            # a[idx], a[l_idx_copy] = a[l_idx_copy], a[idx] # ...then we move the leftmost value to that position, and move the current element value to now former position of the leftmost value, s.t. it's now right of the leftmost value.  
            # l_idx_copy += 1 # increment by one so that if we need to make a swap, the new like value is getting appended to the end of the "like" group.  
        # elif a[idx] > l_element_copy: # or if the current element we're looking at is actually greater than left most value, ... 
            # a[r_idx_copy], a[idx] = a[idx], a[r_idx_copy] # ... then we move the current value to the position of the right most value.  We swap!  E.g., [2,3,9,2,2] to [2,2,9,2,3]
            # r_idx_copy -= 1  # decrement by one so that we don't make redundant swaps on the right.  We're not trying to sort the entire thing, just group elements equal to the left most value together.  
            # idx -= 1 
        # idx += 1
    # return l_idx_copy, r_idx_copy

def partition(arr, l, r, index): 
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



def partition3(a, l, r):
   x, j, t = a[l], l, r
   i = j

   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1 # remain in the same i in this case
      i += 1   
   return j, t

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return 
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    mid_left_idx, mid_right_idx = partition3(a, l, r)
    #use partition3
    #print(m)
    #randomized_quick_sort(a, l, m - 1);
    #randomized_quick_sort(a, m + 1, r);
    randomized_quick_sort(a, l, mid_left_idx - 1)
    randomized_quick_sort(a, mid_right_idx + 1, r) 
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
