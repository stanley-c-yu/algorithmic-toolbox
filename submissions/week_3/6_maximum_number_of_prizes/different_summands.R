# Stanley Yu

optimal_summands <- function(n) {
  summands = c() 
  if (n > 2) {
    prize_value = 1 
    while (prize_value <= 2) {
      summands = append(summands, prize_value)
      prize_value = prize_value + 1 
    }
    summands = append(summands, n - prize_value)
  } else {
    summands = append(summands, n)
  }
  return(summands)
}


print("n = 6")
optimal_summands(6)

print("n=8")
optimal_summands(8)

print("n=2")
optimal_summands(2)
