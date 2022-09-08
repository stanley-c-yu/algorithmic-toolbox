def mergesort(arr, l, r):
    sorted_arr = []
    left_arr = split(arr, l, r)
    right_arr = split(arr, l, r)



def split(arr, l, r): 
    if len(arr) == 1 or len(arr) == 0:
        return arr 
    mp = l + (r - l) // 2
    split(arr[l:mp], l, mp)
    split(arr[mp:], mp, r)
