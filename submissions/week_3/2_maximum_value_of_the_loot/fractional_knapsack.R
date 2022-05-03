# Stanley Yu
# Coursera, Algorithmic Toolbox 
# Greedy Algorithms 

get_optimal_value <- function(capacity, weights, values) {
  # Input: 
  #   capacity: the total weight that knapsack can hold
  #   weights: an array of weights for each of the n items 
  #   values: an array of values for each of the n items.  
  # Output: 
  #   The maximum value of fractions of items that fit into the knapsack.  
  
  value = 0.0000 # Initial value
  val_wgt_ratios = values/weights # Create a vector/list of value-to-weight ratios
  df = data.frame(ratio = val_wgt_ratios, value = values, weight = weights) # create a dataframe of the three vectors
  df = df[order(df$ratio, decreasing = TRUE),] # rearrange everything in decreasing order of ratios
  
  runs = length(values)
  index_col = 1
  
  while (index_col <= runs) {
    if (capacity == 0) {
      return(round(value, digits = 4))
    }
    weight_to_add = min(c(df[index_col,3], capacity))
    value = value + df[index_col, 1]*weight_to_add
    capacity = capacity - weight_to_add 
    index_col = index_col + 1
  }
  return(round(value, digits = 4))
}

#get_optimal_value(50, c(20, 50, 30), c(60, 100, 120))
#get_optimal_value(10, c(30), c(500))