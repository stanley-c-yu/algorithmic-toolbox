def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_product = 0
    numbers.sort() 
    max_product = numbers[n-1] * numbers[n-2]
    return max_product
    
def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product