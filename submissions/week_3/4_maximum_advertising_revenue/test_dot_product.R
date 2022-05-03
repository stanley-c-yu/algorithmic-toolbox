library(testthat)
source("C:/Users/syu01/Documents/code/algorithms/submissions/week_3/4_maximum_advertising_revenue/dot_product.R")


test_that("One Ad with 39 clicks", {
  expect_equal(max_dot_product(c(23), c(39)), 897)
})

test_that("Multiple ads and negative values", {
  expect_equal(max_dot_product(c(1, 3, -5), c(-2, 4, 1)), 23)
})
