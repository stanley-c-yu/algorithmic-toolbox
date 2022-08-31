function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max + 1));
}

function partition3(arr, l, r) {
    let i = l;
    let l_copy = l;
    let r_copy = r;
    let pivot_value = arr[l];
    while (i <= r_copy) {
        //code block to be execute
        if (arr[i] < pivot_value) {
            // code block
            [arr[i], arr[l_copy]] = [arr[l_copy], arr[i]];
            l_copy += 1;
        } else if (arr[i] > pivot_value) {
            [arr[i], arr[r_copy]] = [arr[r_copy], arr[i]];
            r_copy -= 1;
            i -= 1;
        }
        i += 1;
    }
    return [l_copy, r_copy];
}

function randomized_quick_sort(arr, l, r) {
    if (l >= r) {
        return
    }
    let k = getRndInteger(min = l, max = r);
    [arr[l], arr[k]] = [arr[k], arr[l]];
    let [pivot_start, pivot_end] = partition3(arr = arr, l = l, r = r);
    randomized_quick_sort(arr = arr, l = l, r = (pivot_start - 1))
    randomized_quick_sort(arr = arr, l = (pivot_end + 1), r = r)
    return arr
}


// Test 1 
console.log("Test 1: Does the getRndInteger function return an integer that is inclusively within the bounds of min and max?")
let random_int = getRndInteger(0, 4);
if ([0, 1, 2, 3, 4].includes(random_int)) {
    console.log("Test passed.  Element is found within array of possible results.");
} else {
    console.log("Test failed.  Element is not within array, or some other error.");
}

// Test 2
console.log("Test 2: Can Partition3 correctly return the indices marking the boundaries of the pivot partition?")
let arr = [2, 3, 9, 2, 2];
let [left_result, right_result] = partition3(arr = arr, l = 0, r = 4);
if (left_result == 0 && right_result == 2) {
    console.log("Test passed.");
} else {
    console.log("Test failed.");
}

// Test 3
console.log("Test 3: Can Randomized Quick Sort return a correctly sorted array?")
let sorted_arr = randomized_quick_sort(arr = arr, l = 0, r = 4);
if (JSON.stringify(sorted_arr) == JSON.stringify([2, 2, 2, 3, 9])) {
    console.log("Test passed.  The returned array has been sorted correctly in ascending order.");
} else {
    console.log("Test failed.  The array was not correctly sorted in ascending order, or some other error occurred.");
}
