# Stanley Yu 
# Coursera, Algorithmic Toolbox, Greedy Algorithms 
# Covering Segments Problem 

optimal_points <- function(segments) {
  points = list()
  segments = segments[order(sapply(segments, function(x) x[[1]]))]
  points = append(points, segments[[1]][2])
  for (segment in segments) {
    current_point = points[length(points)][[1]][1]
    if (segment[1] >= current_point & segment[1] != current_point) {
      points = append(points, segment[2])
    }
    else if (segment[1] <= current_point & segment[2] <= current_point) {
      points = replace(points, length(points), segment[2])
    }
  }

  return(points)
}

# Tests
optimal_points(list(c(1,3), c(2,5), c(3,6))) # correct answer is 3
optimal_points(list(c(4,7), c(1,3), c(2,5), c(5,6))) # correct answer is 3, 6