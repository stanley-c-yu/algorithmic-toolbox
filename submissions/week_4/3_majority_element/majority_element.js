function majority_element(arr, left, right) {
	if (left == right) {
		return -1 
	}
	if (left + 1 == right) {
		return arr.slice(0, left + 1)
	}
	let left_candidate = majority_element(arr, left, left + Math.floor((right - left) / 2))
	let right_candidate = majority_element(arr, left + Math.floor((right - left) / 2), right)
	let left_count = 0
	let right_count = 0 
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] == left_candidate) {
			left_count += 1
		}
		else if (arr[i] == right_candidate) {
			right_count += 1
		}
		if (left_count > Math.floor(arr.length / 2) ) {
			return left_candidate
		}
		if (right_count > Math.floor(arr.length / 2) ) {
			return right_candidate
		}
	}
	return -1 
}


console.log(majority_element([2, 3, 9, 2, 2], 0, 4))
console.log(majority_element([1, 2, 3, 4], 0, 3))
console.log(majority_element([1, 2, 3, 1], 0, 3))