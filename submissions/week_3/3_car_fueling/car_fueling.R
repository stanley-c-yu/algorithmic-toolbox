# Stanley Yu
# Coursera, Algorithmic Toolbox
# Greedy Algorithms 

compute_min_refills <- function(distance, mileage, stops) {
  # Inputs
  #   distance: an integer representing the distance between the start and ending positions 
  #   mileage: an integer representg the mileage 
  #   stops:  an array of gas stations we can re-fuel at along the way from start to end 
  # Output
  #   The minimum number of stops you'll need to make, or -1 if the journey is impossible.  
  stops = c(0, stops)
  stops = c(stops, distance)
  refills = 0
  position = 1
  most_recent = position 
  while (stops[position] != distance) {
    if ( (stops[position+1] - stops[most_recent]) <= mileage) {
      position = position + 1
    }
    else if (position == most_recent) {
      return(-1)
    } 
    else {
      refills = refills + 1
      most_recent = position
    }
  }
  return(refills)
}


#compute_min_refills(950, 400, c(200, 375, 550, 750))