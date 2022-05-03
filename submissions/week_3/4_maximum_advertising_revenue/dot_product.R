# Stanley Yu
# Coursera, Algorithmic Toolbox
# Greedy Algorithms 

max_dot_product <- function(a, b) {
  a = sort(a, decreasing = TRUE)
  b = sort(b, decreasing = TRUE)
  revenue = 0 
  index = 1
  for (i in a) {
    revenue = revenue + (i * b[index])
    index = index + 1
  }
  
  return(revenue)
}

# max_dot_product(c(23), c(39))
# max_dot_product(c(1, 3, -5), c(-2, 4, 1))