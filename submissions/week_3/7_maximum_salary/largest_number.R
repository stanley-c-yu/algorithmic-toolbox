# Stanley Yu 
# Coursera - Algorithmic Toolbox 

largest_number <- function(digits) {
  answer = "" 
  digits = sort(digits)
  answer_len = 0 
  for (digit in digits) {
    if (answer_len == 0) {
      answer = paste0(answer, toString(digit))
      answer_len = answer_len + 1
    } 
    else {
      orthodox = as.integer(paste0(answer, toString(digit)))
      unorthodox = as.integer(paste0(toString(digit), answer))
      if (orthodox >= unorthodox) {
        answer = toString(orthodox)
      }
      else {
        answer = toString(unorthodox)
      }
    }
  }
  return(answer)
}