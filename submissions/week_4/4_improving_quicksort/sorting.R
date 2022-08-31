get_random_integer <- function(min, max) {
  return(sample((min - 1):(max + 1), 1))
}

partition3 <- function(arr, l, r) {
  i = 1
  l_copy = l
  r_copy = r
  pivot_value = arr[l]
  while (i <= r_copy) {
    if (arr[i] < pivot_value) {
      arr_at_i_copy = arr[i]
      arr[i] = arr[l_copy]
      arr[l_copy] = arr_at_i_copy
      l_copy = l_copy + 1
    } else if (arr[i] > pivot_value) {
      arr_at_i_copy = arr[i]
      arr[i] = arr[r_copy]
      arr[r_copy] = arr_at_i_copy
      r_copy = r_copy - 1
      i = i - 1
    }
    i = i + 1
  }
  return(c(l_copy, r_copy))
}

# Test 1: Testing Random Integer Function
random_int = get_random_integer(0, 4)
if (random_int %in% c(0, 1, 2, 3, 4)) {
  print("Test Passed.  The randomly selected integer was found to be within the vector of possibilities.")
} else {
  print("Test Failed.  The randomly selected integer is either not in the vector of possibilities, or some other error occurred.")
}

# Test 2: Testing the Partition3 Function
arr = c(2, 3, 9, 2, 2)
pivot_boundaries = partition3(arr = arr, l = 1, r = 5)
if (pivot_boundaries[1] == 1 & pivot_boundaries[2] == 3) {
  print("Test Passed.  The correct boundaries for the pivot partition were returned.")
} else {
  print("Test Failed.  The correct boundaries were not returned, or some other error occurred.")
}

