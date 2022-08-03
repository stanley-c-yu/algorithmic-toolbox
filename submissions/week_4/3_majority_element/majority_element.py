# Uses python3
import sys

def get_majority_element(arr, left, right):
    if left == right:
        return -1
    if left + 1 == right: # prevents an endless recursion 
        return arr[left]
    #write your code here
    left_candidate = get_majority_element(arr, left, left + (right - left) // 2) # the MP is defined this way to prevent an overflow error
    right_candidate = get_majority_element(arr, left + (right - left) // 2, right) 
    left_count, right_count = 0, 0 
    for i in arr: 
        if i == left_candidate:
            left_count += 1 
        elif i == right_candidate: 
            right_count += 1 
        if left_count > len(arr) // 2:
            return left_candidate 
        if right_count > len(arr) // 2: 
            return right_candidate 
            
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
