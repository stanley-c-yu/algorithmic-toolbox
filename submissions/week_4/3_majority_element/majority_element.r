majority_element <- function(arr, left, right) {
	if (left == right) {
		return(-1)
	}
	if (left + 1 == right) {
		return(arr[c(left)])
	}
	left_candidate <- majority_element(arr, left, left + floor((right - left) / 2) )
	right_candidate <- majority_element(arr, left + floor((right - left) / 2), right )
	left_count <- 0 
	right_count <- 0 
	for (i in arr) {
		if (i == left_candidate) {
			left_count <- left_count + 1
		}
		else if (i == right_candidate) {
			right_count <- right_count + 1
		}
		if (left_count > floor(length(arr) / 2)) {
			return(left_candidate)
		}
		if (right_count > floor(length(arr) / 2)) {
			return(right_candidate)
		}
	}
	return(-1)
}


majority_element(c(2, 3, 9, 2, 2), 1, 5)
majority_element(c(1, 2, 3, 4), 1, 4)
majority_element(c(1, 2, 3, 1), 1, 4)