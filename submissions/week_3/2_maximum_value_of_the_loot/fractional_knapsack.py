# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    # Input: 
    #   capacity: the total weight that a knapsack can hold 
    #   weights: an array of weights for each of the n items 
    #   values: an array of values for each of the n items.  
    # Output: 
    #   The maximum value of fractions of items that fit into the knapsack. 

    value = 0.
    # write your code here
    
    val_wgt_ratios = [i/j for i, j in zip(values, weights)]
    items = {}
    i = 0 
    # create a dictionary of items where keys are the value-to-weight ratios and values are lists where the first variable is the item's weight and the second is its value (i.e., utility).  
    for ratio in val_wgt_ratios:
        items[ratio] = [weights[i], values[i]]
        i += 1
    
    # iterate through the items in sorted order to max efficiency 
    for item_ratio in sorted(items.keys(), reverse=True):
        if capacity == 0.:
            return round(value, 4)
        # determine the weight to add to the knapsack.  
        #   Equal to cap minus whatever is smallest, the weight of the current item or the remaining capacity
        weight_to_add = min(items[item_ratio][0], capacity)
        # update the value of the knapsack's contents.  
        #   It will either be the full value if we take the entire item, or a fraction of it.  
        value = value + weight_to_add*(item_ratio)
        # update the capacity 
        capacity = capacity - weight_to_add
        
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
