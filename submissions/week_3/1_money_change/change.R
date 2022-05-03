# Stanley Yu
# Coursera, Algorithmic Toolbox
# Greedy Algorithms 

get_change <- function(m) {
  #Input: A single integer m, where m is at least greater than or equal to 1.  
  #Output: The minimum number of coins with denominations 1, 5, 10 that changes m.
  coins = 0 
  while (m != 0) {
    if (m >= 10) {
      m = m - 10 
    } 
    else if (m >= 5 & m < 10) {
      m = m - 5
    }
    else {
      m = m - 1
    }
   coins = coins + 1 
  }
  return(coins)
}

#get_change(2)
#get_change(28)