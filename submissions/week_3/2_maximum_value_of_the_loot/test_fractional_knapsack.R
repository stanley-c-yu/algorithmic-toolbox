library(testthat)
source("C:/Users/syu01/Documents/code/algorithms/submissions/week_3/2_maximum_value_of_the_loot/fractional_knapsack.R")


test_that("Test One", {
  expect_identical(get_optimal_value(50, c(20, 50, 30), c(60, 100, 120)), 180.0000 )
})


test_that("Test Two", {
  expect_identical(get_optimal_value(10, c(30), c(500)), 166.6667)
})